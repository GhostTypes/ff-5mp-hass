/**
 * FlashForge job card.
 *
 * A port of the FlashForgeUI job picker and its material-matching dialog:
 * browse the files on the printer, pick one, map each of its tools to a
 * Material Station slot, and start the print.
 *
 * Vanilla custom element on purpose - no build step, no bundler, no runtime
 * dependency on Home Assistant frontend internals. The file committed to the
 * repository is the file that ships.
 *
 * All data comes from the integration's websocket commands; the card holds no
 * state the printer does not. The matching rules enforced here (material must
 * match, empty and assigned slots unusable, every tool mapped) are duplicated
 * server-side in job.py, which is the side that actually decides - these exist
 * to explain the rules while the user clicks, not to be trusted.
 */

const CARD_VERSION = "1.4.0";

console.info(
  `%c FLASHFORGE-JOB-CARD %c ${CARD_VERSION} `,
  "color: white; background: #f7761f; font-weight: 700;",
  "color: #f7761f; background: white; font-weight: 700;"
);

/* ------------------------------------------------------------------ */
/* Helpers                                                             */
/* ------------------------------------------------------------------ */

const normalize = (value) => (value || "").trim().toLowerCase();

const materialsMatch = (toolMaterial, slotMaterial) =>
  Boolean(toolMaterial) && normalize(toolMaterial) === normalize(slotMaterial);

const colorsDiffer = (toolColor, slotColor) =>
  Boolean(toolColor) && normalize(toolColor) !== normalize(slotColor);

/** Seconds to a compact "1h 42m" / "22m" / "45s". */
function formatDuration(seconds) {
  if (!seconds || seconds <= 0) return "";
  const totalMinutes = Math.round(seconds / 60);
  if (totalMinutes <= 0) return `${Math.max(seconds, 1)}s`;
  const hours = Math.floor(totalMinutes / 60);
  const minutes = totalMinutes % 60;
  if (hours > 0) return minutes > 0 ? `${hours}h ${minutes}m` : `${hours}h`;
  return `${minutes}m`;
}

function formatWeight(grams) {
  if (grams === null || grams === undefined || grams <= 0) return "";
  return `${grams >= 100 ? Math.round(grams) : grams.toFixed(1)} g`;
}

/** Escape for interpolation into innerHTML. File names come from the printer. */
function esc(value) {
  return String(value === null || value === undefined ? "" : value).replace(
    /[&<>"']/g,
    (char) =>
      ({
        "&": "&amp;",
        "<": "&lt;",
        ">": "&gt;",
        '"': "&quot;",
        "'": "&#39;",
      })[char]
  );
}

/** A CSS color for a swatch, falling back to a muted tile when unknown. */
function swatchColor(hex) {
  return /^#[0-9a-f]{6}$/i.test(hex || "") ? hex : "var(--disabled-text-color)";
}

/* ------------------------------------------------------------------ */
/* Strings                                                             */
/* ------------------------------------------------------------------ */

/**
 * The card's copy lives in `frontend/translations/<language>.json`, served
 * from the same static path as this file and fetched at runtime. It cannot
 * live in the integration's `strings.json`: that localizes entities and config
 * flows, and the Home Assistant frontend never hands it to a custom card.
 *
 * Adding a language is therefore one step - copy `en.json`, translate the
 * values, name it after the language code. No change to this file, and no
 * change to the Python.
 *
 * `en.json` is the complete set and the per-key fallback, so a partial or
 * outdated translation degrades one string at a time instead of blanking the
 * card.
 */
const TRANSLATION_BASE = "/flashforge_frontend/translations";
const FALLBACK_LANGUAGE = "en";

/**
 * Language code -> a promise of its table (null when there is no such file).
 * Module-level, so ten cards on one dashboard share a single fetch, and a
 * language already loaded resolves without touching the network again.
 *
 * Only outcomes worth keeping are kept: a 404 is cached, because the answer
 * will not change until the integration is updated (which changes the `?v=`
 * anyway), but a failed request is dropped so the next caller retries. Caching
 * the failure would pin the card to English - or to nothing - for the entire
 * life of the page over one blip while Home Assistant was restarting.
 */
const _tables = new Map();

/** Backoff between retries, in milliseconds; its length caps the attempts. */
const RETRY_DELAYS = [500, 2000, 5000];

function loadTable(language) {
  if (!_tables.has(language)) {
    _tables.set(
      language,
      fetch(`${TRANSLATION_BASE}/${language}.json?v=${CARD_VERSION}`)
        .then((response) => {
          // No such language. A settled fact, worth caching.
          if (response.status === 404) return null;
          if (!response.ok) throw new Error(`HTTP ${response.status}`);
          return response.json();
        })
        .catch((err) => {
          _tables.delete(language);
          throw err;
        })
    );
  }
  return _tables.get(language);
}

/** `loadTable` with backoff; null once the attempts are spent. */
async function loadTableWithRetry(language) {
  for (let attempt = 0; ; attempt++) {
    try {
      return await loadTable(language);
    } catch (err) {
      if (attempt >= RETRY_DELAYS.length) {
        console.warn(
          `flashforge-job-card: could not load ${language} translations`,
          err
        );
        return null;
      }
      await new Promise((resolve) => setTimeout(resolve, RETRY_DELAYS[attempt]));
    }
  }
}

/**
 * Build a translator for a Home Assistant language tag.
 *
 * Only the primary subtag is requested: "de-CH" loads de.json. No regional
 * variants ship, and probing for one would put a 404 in the console on every
 * card load for no gain.
 */
async function translatorFor(language) {
  const tag =
    String(language || "").toLowerCase().split("-")[0] || FALLBACK_LANGUAGE;

  const base = await loadTableWithRetry(FALLBACK_LANGUAGE);
  const table =
    tag === FALLBACK_LANGUAGE ? base : (await loadTableWithRetry(tag)) || base;

  const t = (key, vars) => {
    let text;
    if (table && table[key] !== undefined) text = table[key];
    else if (base && base[key] !== undefined) text = base[key];
    // Last resort: the key itself. Only reachable if the files could not be
    // served at all, since the tests hold every language to English's key set.
    // An odd-looking label beats a blank card, which reads as a broken
    // integration rather than a missing download.
    else return key;
    if (vars) {
      for (const [name, value] of Object.entries(vars)) {
        text = text.split(`{${name}}`).join(String(value));
      }
    }
    return text;
  };

  /** The `_one` / `_other` form of `base` for `count`, also passed as {count}. */
  t.plural = (key, count, vars) =>
    t(`${key}_${count === 1 ? "one" : "other"}`, { count, ...vars });

  return t;
}

/** Stand-in until the tables land; renders empty rather than raw key names. */
function pendingTranslator() {
  const t = () => "";
  t.plural = () => "";
  return t;
}

/* ------------------------------------------------------------------ */
/* Styles                                                              */
/* ------------------------------------------------------------------ */

const STYLES = `
  :host { display: block; }
  ha-card { overflow: hidden; }
  .header {
    display: flex; align-items: center; justify-content: space-between;
    padding: 16px 16px 8px; gap: 8px;
  }
  .title { font-size: 1.2rem; font-weight: 500; color: var(--primary-text-color); }
  .subtitle { font-size: 0.8rem; color: var(--secondary-text-color); }
  .icon-button {
    background: none; border: none; cursor: pointer; padding: 6px; border-radius: 50%;
    color: var(--secondary-text-color); font-size: 1.1rem; line-height: 1;
  }
  .icon-button:hover { background: var(--secondary-background-color); }

  .body { padding: 0 8px 8px; }
  .message {
    padding: 16px; color: var(--secondary-text-color); font-size: 0.95rem; text-align: center;
  }
  .message.error { color: var(--error-color); }

  .file {
    display: flex; align-items: center; gap: 12px; padding: 10px 8px;
    border-radius: 10px; cursor: pointer; border: 2px solid transparent;
  }
  .file:hover { background: var(--secondary-background-color); }
  .file.selected {
    border-color: var(--primary-color);
    background: color-mix(in srgb, var(--primary-color) 12%, transparent);
  }
  .thumb {
    width: 56px; height: 56px; flex: 0 0 56px; border-radius: 8px;
    background: var(--secondary-background-color); object-fit: contain;
    display: flex; align-items: center; justify-content: center;
    color: var(--disabled-text-color); font-size: 1.4rem;
  }
  .file-info { flex: 1; min-width: 0; }
  .file-name {
    color: var(--primary-text-color); font-weight: 500;
    overflow: hidden; text-overflow: ellipsis; white-space: nowrap;
  }
  .file-meta {
    display: flex; align-items: center; gap: 6px; flex-wrap: wrap;
    color: var(--secondary-text-color); font-size: 0.82rem; margin-top: 3px;
  }
  .dot { opacity: 0.6; }
  .tool-swatches { display: inline-flex; gap: 3px; align-items: center; }
  .swatch {
    width: 12px; height: 12px; border-radius: 3px;
    border: 1px solid var(--divider-color); display: inline-block;
  }

  .footer {
    display: flex; align-items: center; justify-content: space-between;
    gap: 12px; padding: 8px 16px 16px; flex-wrap: wrap;
  }
  .leveling { display: flex; align-items: center; gap: 8px; color: var(--primary-text-color); font-size: 0.9rem; }
  button.primary {
    background: var(--primary-color); color: var(--text-primary-color, #fff);
    border: none; border-radius: 8px; padding: 10px 18px; font-size: 0.95rem;
    font-weight: 500; cursor: pointer;
  }
  button.primary:disabled { background: var(--disabled-text-color); cursor: not-allowed; }
  button.secondary {
    background: none; color: var(--primary-color); border: none;
    border-radius: 8px; padding: 10px 16px; font-size: 0.95rem; cursor: pointer;
  }

  /* Modal ---------------------------------------------------------- */
  .backdrop {
    position: fixed; inset: 0; background: rgba(0, 0, 0, 0.6);
    display: flex; align-items: center; justify-content: center; z-index: 9;
    padding: 16px;
  }
  .modal {
    background: var(--card-background-color, #fff); color: var(--primary-text-color);
    border-radius: 14px; width: min(720px, 100%); max-height: 88vh;
    display: flex; flex-direction: column; box-shadow: 0 8px 32px rgba(0,0,0,0.35);
  }
  .modal-header {
    padding: 16px 20px; border-bottom: 1px solid var(--divider-color);
    display: flex; align-items: center; justify-content: space-between; gap: 8px;
  }
  .modal-title { font-size: 1.05rem; font-weight: 500; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }
  .modal-body { padding: 16px 20px; overflow-y: auto; }
  .modal-footer {
    padding: 12px 16px; border-top: 1px solid var(--divider-color);
    display: flex; justify-content: flex-end; gap: 8px;
  }

  .panes { display: flex; gap: 16px; }
  @media (max-width: 560px) { .panes { flex-direction: column; } }
  .pane { flex: 1; min-width: 0; }
  .pane-title {
    font-size: 0.78rem; text-transform: uppercase; letter-spacing: 0.06em;
    color: var(--secondary-text-color); margin-bottom: 8px;
  }

  .item {
    border: 2px solid var(--divider-color); border-radius: 10px;
    padding: 10px 12px; margin-bottom: 8px; cursor: pointer;
  }
  .item:hover:not(.disabled) { border-color: var(--primary-color); }
  .item.selected {
    border-color: var(--primary-color);
    background: color-mix(in srgb, var(--primary-color) 14%, transparent);
  }
  .item.mapped { opacity: 0.62; }
  .item.disabled { opacity: 0.42; cursor: not-allowed; }
  .item-header { display: flex; align-items: center; justify-content: space-between; gap: 8px; }
  .item-label { font-weight: 500; }
  .item-detail { font-size: 0.82rem; color: var(--secondary-text-color); margin-top: 2px; }
  .swatch.lg { width: 18px; height: 18px; border-radius: 4px; }

  .mappings { margin-top: 16px; }
  .mapping {
    display: flex; align-items: center; gap: 8px; padding: 7px 10px;
    border-radius: 8px; background: var(--secondary-background-color); margin-bottom: 6px;
  }
  .mapping.warn { box-shadow: inset 0 0 0 2px var(--warning-color, #ffa726); }
  .mapping-text { flex: 1; font-size: 0.9rem; }
  .arrow { opacity: 0.6; margin: 0 4px; }
  .remove {
    background: none; border: none; cursor: pointer; font-size: 1.1rem;
    color: var(--secondary-text-color); line-height: 1; padding: 2px 6px;
  }
  .empty-hint { font-size: 0.85rem; color: var(--secondary-text-color); padding: 6px 2px; }

  .alert { border-radius: 8px; padding: 10px 12px; font-size: 0.86rem; margin-top: 12px; }
  .alert.error { background: color-mix(in srgb, var(--error-color) 18%, transparent); color: var(--error-color); }
  .alert.warning { background: color-mix(in srgb, var(--warning-color, #ffa726) 20%, transparent); color: var(--primary-text-color); }
  .alert.success { background: color-mix(in srgb, var(--success-color, #4caf50) 20%, transparent); color: var(--primary-text-color); }
  .hidden { display: none !important; }

  .summary { display: flex; gap: 14px; align-items: center; margin-bottom: 4px; }
  .summary .thumb { width: 76px; height: 76px; flex-basis: 76px; }
`;

/* ------------------------------------------------------------------ */
/* Card                                                                */
/* ------------------------------------------------------------------ */

class FlashForgeJobCard extends HTMLElement {
  static getConfigElement() {
    return document.createElement("flashforge-job-card-editor");
  }

  static getStubConfig() {
    return {};
  }

  constructor() {
    super();
    this._config = {};
    this._hass = null;
    this._loading = false;
    this._loaded = false;
    this._error = null;
    this._notice = null;
    this._data = null; // { files, slots, model, printer_name, has_material_station }
    this._thumbs = {};
    this._selected = null;
    this._leveling = false;
    this._dialog = null; // matching / confirm dialog state
    this._starting = false;
    this._language = null;
    this._t = pendingTranslator();
  }

  setConfig(config) {
    const previousEntry = this._config.entry_id;
    this._config = config || {};
    this._leveling = Boolean(this._config.leveling_default);
    this._loaded = false;

    // Reconfigured live (the card editor, or a dashboard edit). `hass` is only
    // set once per element, so nothing else would reload the new printer.
    if (this._hass && this._config.entry_id !== previousEntry) {
      this._data = null;
      this._thumbs = {};
      this._selected = null;
      this._render();
      this._loadFiles();
    }
  }

  set hass(hass) {
    const first = !this._hass;
    this._hass = hass;

    // `hass` is set on every state change, so only act on a real language
    // change - the user switching their profile language re-renders the card
    // without a reload.
    const language = (hass && hass.locale && hass.locale.language) || null;
    if (language !== this._language) {
      this._language = language;
      this._applyLanguage(language);
    }

    if (first) {
      this._render();
      this._loadFiles();
    }
  }

  /** Swap in the translator for `language`, re-rendering once it has loaded. */
  async _applyLanguage(language) {
    const t = await translatorFor(language);
    // Superseded while the fetch was in flight; the later call owns the card.
    if (language !== this._language) return;
    this._t = t;
    if (this._root) this._render();
  }

  getCardSize() {
    return 8;
  }

  /* -- transport --------------------------------------------------- */

  _send(message) {
    if (!this._hass) return Promise.reject(new Error(this._t("err_not_ready")));
    return this._hass.connection.sendMessagePromise({
      ...message,
      entry_id: this._config.entry_id,
    });
  }

  async _loadFiles() {
    // Nothing to ask for until the card knows which printer it belongs to;
    // _render() is already showing the "pick a printer" message.
    if (!this._config.entry_id) return;

    this._loading = true;
    this._error = null;
    this._render();

    try {
      this._data = await this._send({ type: "flashforge/files/list" });
      this._loaded = true;
      // Drop a selection that the printer no longer lists.
      if (
        this._selected &&
        !this._data.files.some((file) => file.file_name === this._selected)
      ) {
        this._selected = null;
      }
    } catch (err) {
      this._error = err.message || this._t("err_load");
      this._data = null;
    } finally {
      this._loading = false;
      this._render();
      this._loadThumbnails();
    }
  }

  /**
   * Fetch thumbnails one at a time, after the list is on screen. Sequential so
   * a printer with ten files is not hit with ten simultaneous requests while it
   * is also answering the status poll.
   */
  async _loadThumbnails() {
    if (!this._data) return;
    for (const file of this._data.files) {
      if (file.file_name in this._thumbs) continue;
      try {
        const result = await this._send({
          type: "flashforge/file/thumbnail",
          file_name: file.file_name,
        });
        this._thumbs[file.file_name] = result.image || null;
      } catch (err) {
        this._thumbs[file.file_name] = null;
      }
      this._renderFiles();
    }
  }

  /* -- actions ----------------------------------------------------- */

  async _onStartClicked() {
    if (!this._selected) return;
    this._notice = null;

    let prepared;
    try {
      prepared = await this._send({
        type: "flashforge/job/prepare",
        file_name: this._selected,
      });
    } catch (err) {
      this._error = err.message || this._t("err_prepare");
      this._render();
      return;
    }

    if (prepared.requires_matching) {
      const mappings = new Map();
      for (const mapping of prepared.suggested_mappings || []) {
        mappings.set(mapping.tool_id, mapping);
      }
      this._dialog = {
        mode: "match",
        file: prepared.file,
        slots: prepared.slots,
        mappings,
        selectedTool: null,
        error: null,
        warning: null,
      };
    } else {
      this._dialog = {
        mode: "confirm",
        file: prepared.file,
        slots: prepared.slots,
        mappings: new Map(),
        selectedTool: null,
        error: null,
        warning: null,
      };
    }
    this._render();
  }

  _closeDialog() {
    this._dialog = null;
    this._starting = false;
    this._render();
  }

  _onToolClicked(toolId) {
    const dialog = this._dialog;
    if (!dialog) return;
    dialog.selectedTool = dialog.selectedTool === toolId ? null : toolId;
    dialog.error = null;
    this._render();
  }

  _onSlotClicked(slotId) {
    const dialog = this._dialog;
    if (!dialog) return;

    const slot = dialog.slots.find((item) => item.slot_id === slotId);
    if (!slot || slot.is_empty) return;

    if (dialog.selectedTool === null) {
      dialog.error = this._t("err_select_tool_first");
      this._render();
      return;
    }

    const tool = dialog.file.tool_datas.find(
      (item) => item.tool_id === dialog.selectedTool
    );
    if (!tool) return;

    if (!materialsMatch(tool.material_name, slot.material_name)) {
      dialog.error = this._t("err_material_mismatch", {
        tool: tool.tool_id + 1,
        toolMaterial: tool.material_name || this._t("unknown_material_indef"),
        slot: slot.slot_id,
        slotMaterial: slot.material_name || this._t("no_material"),
      });
      this._render();
      return;
    }

    const takenBy = [...dialog.mappings.values()].find(
      (mapping) => mapping.slot_id === slot.slot_id && mapping.tool_id !== tool.tool_id
    );
    if (takenBy) {
      dialog.error = this._t("err_slot_taken", {
        slot: slot.slot_id,
        tool: takenBy.tool_id + 1,
      });
      this._render();
      return;
    }

    dialog.mappings.set(tool.tool_id, {
      tool_id: tool.tool_id,
      slot_id: slot.slot_id,
      material_name: tool.material_name || slot.material_name,
      tool_material_color: tool.material_color,
      slot_material_color: slot.material_color,
    });
    dialog.selectedTool = null;
    dialog.error = null;
    dialog.warning = colorsDiffer(tool.material_color, slot.material_color)
      ? this._t("warn_color", {
          tool: tool.tool_id + 1,
          toolColor: tool.material_color,
          slot: slot.slot_id,
          slotColor: slot.material_color || this._t("unknown_color"),
        })
      : null;
    this._render();
  }

  _onRemoveMapping(toolId) {
    if (!this._dialog) return;
    this._dialog.mappings.delete(toolId);
    this._dialog.error = null;
    this._dialog.warning = null;
    this._render();
  }

  async _onConfirmStart() {
    const dialog = this._dialog;
    if (!dialog || this._starting) return;

    this._starting = true;
    dialog.error = null;
    this._render();

    try {
      const result = await this._send({
        type: "flashforge/job/start",
        file_name: dialog.file.file_name,
        leveling: this._leveling,
        material_mappings: [...dialog.mappings.values()],
      });
      this._dialog = null;
      this._starting = false;
      // The warnings themselves come from the integration, which does not know
      // the user's language - they stay as sent.
      const warnings = result.warnings || [];
      this._notice = {
        type: warnings.length ? "warning" : "success",
        text:
          this._t("notice_started", { file: result.file_name }) +
          (warnings.length ? ` ${warnings.join(" ")}` : ""),
      };
      this._render();
    } catch (err) {
      this._starting = false;
      dialog.error = err.message || this._t("err_start");
      this._render();
    }
  }

  /* -- rendering --------------------------------------------------- */

  _ensureDom() {
    if (this._root) return;
    this._root = this.attachShadow({ mode: "open" });
    this._root.innerHTML = `
      <style>${STYLES}</style>
      <ha-card>
        <div class="header">
          <div>
            <div class="title"></div>
            <div class="subtitle"></div>
          </div>
          <button class="icon-button" id="refresh">&#x21bb;</button>
        </div>
        <div class="body" id="body"></div>
        <div class="footer" id="footer"></div>
      </ha-card>
      <div id="modal-host"></div>
    `;

    this._root.getElementById("refresh").addEventListener("click", () => {
      this._thumbs = {};
      this._notice = null;
      this._loadFiles();
    });
  }

  _render() {
    this._ensureDom();
    // Set here rather than in _ensureDom: that runs once, and the title has to
    // follow a language change.
    this._root.getElementById("refresh").title = this._t("refresh");

    if (!this._config.entry_id) {
      this._root.querySelector(".title").textContent = "FlashForge";
      this._root.querySelector(".subtitle").textContent = "";
      this._root.getElementById("body").innerHTML =
        `<div class="message error">${esc(this._t("no_printer"))}</div>`;
      this._root.getElementById("footer").innerHTML = "";
      this._root.getElementById("modal-host").innerHTML = "";
      return;
    }

    const name =
      this._config.title || (this._data && this._data.printer_name) || "FlashForge";
    this._root.querySelector(".title").textContent = name;
    this._root.querySelector(".subtitle").textContent = this._data
      ? this._t.plural("subtitle", this._data.files.length, {
          model: this._data.model,
        })
      : "";

    this._renderFiles();
    this._renderFooter();
    this._renderModal();
  }

  _renderFiles() {
    if (!this._root) return;
    const body = this._root.getElementById("body");

    if (this._loading && !this._loaded) {
      body.innerHTML = `<div class="message">${esc(this._t("loading"))}</div>`;
      return;
    }
    if (this._error) {
      body.innerHTML = `<div class="message error">${esc(this._error)}</div>`;
      return;
    }
    if (!this._data || this._data.files.length === 0) {
      body.innerHTML = `<div class="message">${esc(this._t("no_files"))}</div>`;
      return;
    }

    body.innerHTML = this._data.files
      .map((file) => this._fileRowHtml(file))
      .join("");

    body.querySelectorAll(".file").forEach((element) => {
      element.addEventListener("click", () => {
        this._selected = element.dataset.file;
        this._notice = null;
        this._render();
      });
    });
  }

  _fileRowHtml(file) {
    const thumb = this._thumbs[file.file_name];
    const meta = [];
    const duration = formatDuration(file.printing_time);
    if (duration) meta.push(esc(duration));
    const weight = formatWeight(file.total_filament_weight);
    if (weight) meta.push(esc(weight));

    const tools = file.tool_datas || [];
    let toolsHtml = "";
    if (tools.length) {
      const swatches = tools
        .map(
          (tool) =>
            `<span class="swatch" style="background:${swatchColor(
              tool.material_color
            )}" title="${esc(
              this._t("tool_swatch_title", {
                tool: tool.tool_id + 1,
                material: tool.material_name || this._t("unknown_lower"),
              })
            )}"></span>`
        )
        .join("");
      toolsHtml = `<span class="tool-swatches">${swatches}</span><span>${esc(
        this._t.plural("tools", tools.length)
      )}</span>`;
    } else if (file.tool_count) {
      toolsHtml = `<span>${esc(this._t.plural("tools", file.tool_count))}</span>`;
    }

    const metaHtml = meta
      .map((part) => `<span>${part}</span>`)
      .join(`<span class="dot">·</span>`);
    const separator = metaHtml && toolsHtml ? `<span class="dot">·</span>` : "";

    return `
      <div class="file ${this._selected === file.file_name ? "selected" : ""}"
           data-file="${esc(file.file_name)}">
        ${
          thumb
            ? `<img class="thumb" src="data:image/png;base64,${thumb}" alt="">`
            : `<div class="thumb">⚙</div>`
        }
        <div class="file-info">
          <div class="file-name" title="${esc(file.file_name)}">${esc(file.file_name)}</div>
          <div class="file-meta">${metaHtml}${separator}${toolsHtml}</div>
        </div>
      </div>`;
  }

  _renderFooter() {
    const footer = this._root.getElementById("footer");
    if (this._error || !this._data || this._data.files.length === 0) {
      footer.innerHTML = "";
      return;
    }

    footer.innerHTML = `
      ${
        this._notice
          ? `<div class="alert ${this._notice.type}" style="flex:1 0 100%">${esc(
              this._notice.text
            )}</div>`
          : ""
      }
      <label class="leveling">
        <input type="checkbox" id="leveling" ${this._leveling ? "checked" : ""}>
        ${esc(this._t("leveling"))}
      </label>
      <button class="primary" id="start" ${this._selected ? "" : "disabled"}>
        ${esc(this._t("start"))}
      </button>`;

    const leveling = this._root.getElementById("leveling");
    if (leveling) {
      leveling.addEventListener("change", (event) => {
        this._leveling = event.target.checked;
      });
    }
    const start = this._root.getElementById("start");
    if (start) start.addEventListener("click", () => this._onStartClicked());
  }

  _renderModal() {
    const host = this._root.getElementById("modal-host");
    if (!this._dialog) {
      host.innerHTML = "";
      return;
    }
    host.innerHTML =
      this._dialog.mode === "match" ? this._matchingHtml() : this._confirmHtml();
    this._wireModal(host);
  }

  _confirmHtml() {
    const file = this._dialog.file;
    const thumb = this._thumbs[file.file_name];
    const bits = [formatDuration(file.printing_time), formatWeight(file.total_filament_weight)]
      .filter(Boolean)
      .join(" · ");

    return `
      <div class="backdrop">
        <div class="modal">
          <div class="modal-header">
            <div class="modal-title">${esc(this._t("confirm_title"))}</div>
            <button class="icon-button" data-action="close">&#x2715;</button>
          </div>
          <div class="modal-body">
            <div class="summary">
              ${
                thumb
                  ? `<img class="thumb" src="data:image/png;base64,${thumb}" alt="">`
                  : `<div class="thumb">⚙</div>`
              }
              <div>
                <div class="file-name">${esc(file.file_name)}</div>
                <div class="item-detail">${esc(bits || this._t("no_metadata"))}</div>
                <div class="item-detail">${esc(
                  this._t("bed_leveling_state", {
                    state: this._t(this._leveling ? "on" : "off"),
                  })
                )}</div>
              </div>
            </div>
            ${
              this._dialog.slots.length === 0 && file.use_matl_station
                ? `<div class="alert warning">${esc(this._t("warn_no_station"))}</div>`
                : ""
            }
            ${this._alertsHtml()}
          </div>
          <div class="modal-footer">
            <button class="secondary" data-action="close">${esc(this._t("cancel"))}</button>
            <button class="primary" data-action="start" ${this._starting ? "disabled" : ""}>
              ${esc(this._t(this._starting ? "starting" : "start"))}
            </button>
          </div>
        </div>
      </div>`;
  }

  _matchingHtml() {
    const dialog = this._dialog;
    const tools = dialog.file.tool_datas || [];
    const allMapped = tools.every((tool) => dialog.mappings.has(tool.tool_id));

    const toolsHtml = tools
      .map((tool) => {
        const mapping = dialog.mappings.get(tool.tool_id);
        return `
          <div class="item ${dialog.selectedTool === tool.tool_id ? "selected" : ""} ${
            mapping ? "mapped" : ""
          }" data-tool="${tool.tool_id}">
            <div class="item-header">
              <span class="item-label">${esc(
                this._t("tool_n", { tool: tool.tool_id + 1 })
              )}</span>
              <span class="swatch lg" style="background:${swatchColor(tool.material_color)}"></span>
            </div>
            <div class="item-detail">${esc(
              tool.material_name || this._t("unknown_material")
            )}${
              tool.filament_weight ? ` · ${formatWeight(tool.filament_weight)}` : ""
            }</div>
            ${
              mapping
                ? `<div class="item-detail">${esc(
                    this._t("mapped_to", { slot: mapping.slot_id })
                  )}</div>`
                : ""
            }
          </div>`;
      })
      .join("");

    const slotsHtml = dialog.slots
      .map((slot) => {
        const assigned = [...dialog.mappings.values()].some(
          (mapping) => mapping.slot_id === slot.slot_id
        );
        const disabled = slot.is_empty || assigned;
        return `
          <div class="item ${disabled ? "disabled" : ""}" data-slot="${slot.slot_id}">
            <div class="item-header">
              <span class="item-label">${esc(
                this._t("slot_n", { slot: slot.slot_id })
              )}</span>
              <span class="swatch lg" style="background:${swatchColor(slot.material_color)}"></span>
            </div>
            <div class="item-detail">${
              slot.is_empty
                ? esc(this._t("empty"))
                : esc(slot.material_name || this._t("unknown")) +
                  (assigned ? esc(this._t("assigned_suffix")) : "")
            }</div>
          </div>`;
      })
      .join("");

    const mappingsHtml = dialog.mappings.size
      ? [...dialog.mappings.values()]
          .sort((a, b) => a.tool_id - b.tool_id)
          .map(
            (mapping) => `
              <div class="mapping ${
                colorsDiffer(mapping.tool_material_color, mapping.slot_material_color)
                  ? "warn"
                  : ""
              }">
                <span class="swatch" style="background:${swatchColor(
                  mapping.tool_material_color
                )}"></span>
                <span class="mapping-text">${esc(
                  this._t("tool_n", { tool: mapping.tool_id + 1 })
                )}
                  <span class="arrow">→</span> ${esc(
                    this._t("slot_n", { slot: mapping.slot_id })
                  )}</span>
                <span class="swatch" style="background:${swatchColor(
                  mapping.slot_material_color
                )}"></span>
                <button class="remove" data-remove="${mapping.tool_id}" title="${esc(
                  this._t("remove")
                )}">&#x2715;</button>
              </div>`
          )
          .join("")
      : `<div class="empty-hint">${esc(this._t("mapping_hint"))}</div>`;

    return `
      <div class="backdrop">
        <div class="modal">
          <div class="modal-header">
            <div class="modal-title" title="${esc(dialog.file.file_name)}">
              ${esc(this._t("match_title", { file: dialog.file.file_name }))}
            </div>
            <button class="icon-button" data-action="close">&#x2715;</button>
          </div>
          <div class="modal-body">
            <div class="panes">
              <div class="pane">
                <div class="pane-title">${esc(this._t("pane_needs"))}</div>
                ${
                  toolsHtml ||
                  `<div class="empty-hint">${esc(this._t("no_tool_data"))}</div>`
                }
              </div>
              <div class="pane">
                <div class="pane-title">${esc(this._t("pane_station"))}</div>
                ${
                  slotsHtml ||
                  `<div class="empty-hint">${esc(this._t("no_slots"))}</div>`
                }
              </div>
            </div>
            <div class="mappings">
              <div class="pane-title">${esc(this._t("pane_mappings"))}</div>
              ${mappingsHtml}
            </div>
            ${this._alertsHtml()}
          </div>
          <div class="modal-footer">
            <button class="secondary" data-action="close">${esc(this._t("cancel"))}</button>
            <button class="primary" data-action="start" ${
              allMapped && !this._starting ? "" : "disabled"
            }>${esc(this._t(this._starting ? "starting" : "start"))}</button>
          </div>
        </div>
      </div>`;
  }

  _alertsHtml() {
    const dialog = this._dialog;
    return `
      ${dialog.error ? `<div class="alert error">${esc(dialog.error)}</div>` : ""}
      ${dialog.warning ? `<div class="alert warning">${esc(dialog.warning)}</div>` : ""}`;
  }

  _wireModal(host) {
    host.querySelectorAll('[data-action="close"]').forEach((element) =>
      element.addEventListener("click", () => this._closeDialog())
    );
    host.querySelectorAll('[data-action="start"]').forEach((element) =>
      element.addEventListener("click", () => this._onConfirmStart())
    );
    host.querySelectorAll("[data-tool]").forEach((element) =>
      element.addEventListener("click", () =>
        this._onToolClicked(Number(element.dataset.tool))
      )
    );
    host.querySelectorAll("[data-slot]").forEach((element) => {
      if (element.classList.contains("disabled")) return;
      element.addEventListener("click", () =>
        this._onSlotClicked(Number(element.dataset.slot))
      );
    });
    host.querySelectorAll("[data-remove]").forEach((element) =>
      element.addEventListener("click", (event) => {
        event.stopPropagation();
        this._onRemoveMapping(Number(element.dataset.remove));
      })
    );
    const backdrop = host.querySelector(".backdrop");
    if (backdrop) {
      backdrop.addEventListener("click", (event) => {
        if (event.target === backdrop) this._closeDialog();
      });
    }
  }
}

/* ------------------------------------------------------------------ */
/* Config editor                                                       */
/* ------------------------------------------------------------------ */

class FlashForgeJobCardEditor extends HTMLElement {
  constructor() {
    super();
    this._language = null;
    this._t = pendingTranslator();
  }

  setConfig(config) {
    this._config = { ...config };
    this._render();
  }

  set hass(hass) {
    this._hass = hass;

    const language = (hass && hass.locale && hass.locale.language) || null;
    if (language !== this._language) {
      this._language = language;
      this._applyLanguage(language);
    }

    this._loadEntries();
  }

  async _applyLanguage(language) {
    const t = await translatorFor(language);
    if (language !== this._language) return;
    this._t = t;
    if (this._root) this._render();
  }

  async _loadEntries() {
    if (this._entries || !this._hass) return;
    try {
      const result = await this._hass.connection.sendMessagePromise({
        type: "flashforge/entries",
      });
      this._entries = result.entries || [];
    } catch (err) {
      this._entries = [];
    }
    this._render();
  }

  _emit(config) {
    this._config = config;
    this.dispatchEvent(
      new CustomEvent("config-changed", {
        detail: { config },
        bubbles: true,
        composed: true,
      })
    );
  }

  _render() {
    if (!this._root) {
      this._root = this.attachShadow({ mode: "open" });
    }
    const entries = this._entries || [];
    const selected = (this._config && this._config.entry_id) || "";

    this._root.innerHTML = `
      <style>
        .field { display: block; margin-bottom: 14px; }
        .label { font-size: 0.85rem; color: var(--secondary-text-color); margin-bottom: 4px; }
        select, input {
          width: 100%; padding: 8px; border-radius: 6px; box-sizing: border-box;
          border: 1px solid var(--divider-color);
          background: var(--card-background-color); color: var(--primary-text-color);
        }
      </style>
      <label class="field">
        <div class="label">${esc(this._t("editor_printer"))}</div>
        <select id="entry">
          <option value="">${esc(this._t("editor_select"))}</option>
          ${entries
            .map(
              (entry) =>
                `<option value="${esc(entry.entry_id)}" ${
                  entry.entry_id === selected ? "selected" : ""
                }>${esc(entry.title)}</option>`
            )
            .join("")}
        </select>
      </label>
      <label class="field">
        <div class="label">${esc(this._t("editor_title"))}</div>
        <input id="title" type="text" value="${esc(
          (this._config && this._config.title) || ""
        )}">
      </label>`;

    this._root.getElementById("entry").addEventListener("change", (event) => {
      this._emit({ ...this._config, entry_id: event.target.value || undefined });
    });
    this._root.getElementById("title").addEventListener("change", (event) => {
      const title = event.target.value.trim();
      const config = { ...this._config };
      if (title) config.title = title;
      else delete config.title;
      this._emit(config);
    });
  }
}

// Home Assistant replaces `window.customElements` with its own scoped registry
// while the frontend boots. This module is injected into the document by
// `add_extra_js_url`, so it runs *before* that swap - defining the elements only
// here puts them in a registry the frontend then stops consulting. The failure
// is silent and misleading: no console error, `window.customCards` carries the
// picker entry (it lives on `window`, not on the registry), and any dashboard
// using the card reports "custom element doesn't exist". Cards loaded as
// Lovelace resources are unaffected because those are fetched after the boot.
//
// So: define into whatever registry is current, and again if the frontend
// exchanges it. Every call is guarded, so a browser that never swaps registers
// exactly once.
const ELEMENTS = [
  ["flashforge-job-card", FlashForgeJobCard],
  ["flashforge-job-card-editor", FlashForgeJobCardEditor],
];

function defineOnce(name, constructor) {
  if (customElements.get(name)) return;
  try {
    customElements.define(name, constructor);
  } catch (err) {
    // A registry may refuse a constructor another registry already used. A
    // fresh subclass behaves identically and is accepted.
    customElements.define(name, class extends constructor {});
  }
}

function registerElements() {
  for (const [name, constructor] of ELEMENTS) defineOnce(name, constructor);
}

registerElements();

// The swap happens during the frontend's bootstrap, for which this module has
// no event to listen to. Watch for the registry object being exchanged, and
// stop after a minute so a page that never swaps does not poll forever.
const REGISTRY_POLL_MS = 200;
const REGISTRY_TIMEOUT_MS = 60000;
const initialRegistry = window.customElements;
let registryWaited = 0;
const registryWatch = setInterval(() => {
  registryWaited += REGISTRY_POLL_MS;
  if (window.customElements !== initialRegistry) {
    registerElements();
    clearInterval(registryWatch);
  } else if (registryWaited >= REGISTRY_TIMEOUT_MS) {
    clearInterval(registryWatch);
  }
}, REGISTRY_POLL_MS);

// English only, unavoidably: this runs at module load, before any element is
// constructed and before `hass` (and therefore the user's language) exists.
// The card picker reads it synchronously, so there is nothing to await.
window.customCards = window.customCards || [];
window.customCards.push({
  type: "flashforge-job-card",
  name: "FlashForge Print Job",
  description:
    "Browse the files on a FlashForge printer, match materials to the Material Station, and start a print.",
  preview: false,
  documentationURL: "https://github.com/GhostTypes/ff-5mp-hass",
});
