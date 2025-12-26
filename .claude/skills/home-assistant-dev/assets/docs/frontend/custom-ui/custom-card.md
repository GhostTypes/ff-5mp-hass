# Source: https://developers.home-assistant.io/docs/frontend/custom-ui/custom-card

[Dashboards](https://www.home-assistant.io/dashboards/) are our approach to defining your user interface for Home Assistant. We offer a lot of built-in cards, but you're not just limited to the ones that we decided to include in Home Assistant. You can build and use your own!

## Defining your card

This is a basic example to show what's possible.

Create a new file in your Home Assistant config dir as `<config>/www/content-card-example.js` and put in the following contents:

```
class ContentCardExample extends HTMLElement {
  // Whenever the state changes, a new `hass` object is set. Use this to
  // update your content.
  set hass(hass) {
    // Initialize the content if it's not there yet.
    if (!this.content) {
      this.innerHTML = `
        <ha-card header="Example-card">
          <div class="card-content"></div>
        </ha-card>
      `;
      this.content = this.querySelector("div");
    }

    const entityId = this.config.entity;
    const state = hass.states[entityId];
    const stateStr = state ? state.state : "unavailable";

    this.content.innerHTML = `
      The state of ${entityId} is ${stateStr}!
      <br><br>
      <img src="http://via.placeholder.com/350x150">
    `;
  }

  // The user supplied configuration. Throw an exception and Home Assistant
  // will render an error card.
  setConfig(config) {
    if (!config.entity) {
      throw new Error("You need to define an entity");
    }
    this.config = config;
  }

  // The height of your card. Home Assistant uses this to automatically
  // distribute all cards over the available columns in masonry view
  getCardSize() {
    return 3;
  }

  // The rules for sizing your card in the grid in sections view
  getGridOptions() {
    return {
      rows: 3,
      columns: 6,
      min_rows: 3,
      max_rows: 3,
    };
  }
}

customElements.define("content-card-example", ContentCardExample);
```

## Referencing your new card

In our example card we defined a card with the tag `content-card-example` (see last line), so our card type will be `custom:content-card-example`. And because you created the file in your `<config>/www` directory, it will be accessible in your browser via the url `/local/` (if you have recently added the www folder you will need to re-start Home Assistant for files to be picked up).

Add a resource to your dashboard configuration with URL `/local/content-card-example.js` and type `module` ([resource docs](/docs/frontend/custom-ui/registering-resources)).

You can then use your card in your dashboard configuration:

```
# Example dashboard configuration
views:
  - name: Example
    cards:
      - type: "custom:content-card-example"
        entity: input_boolean.switch_tv
```

## API

Custom cards are defined as a [custom element](https://developer.mozilla.org/en-US/docs/Web/Web_Components/Using_custom_elements). It's up to you to decide how to render your DOM inside your element. You can use Polymer, Angular, Preact or any other popular framework (except for React – [more info on React here](https://custom-elements-everywhere.com/#react)).

### Configuration

Home Assistant will call `setConfig(config)` when the configuration changes (rare). If you throw an exception if the configuration is invalid, Home Assistant will render an error card to notify the user.

Home Assistant will set [the `hass` property](/docs/frontend/data/) when the state of Home Assistant changes (frequent). Whenever the state changes, the component will have to update itself to represent the latest state.

### Sizing in masonry view

Your card can define a `getCardSize` method that returns the size of your card as a number or a promise that will resolve to a number. A height of 1 is equivalent to 50 pixels. This will help Home Assistant distribute the cards evenly over the columns in the [masonry view](https://www.home-assistant.io/dashboards/masonry/). A card size of `1` will be assumed if the method is not defined.

Since some elements can be lazy loaded, if you want to get the card size of another element, you should first check it is defined.

```
return customElements
  .whenDefined(element.localName)
  .then(() => element.getCardSize());
```

### Sizing in sections view

You can define a `getGridOptions` method that returns the min, max and default number of cells your card will take in the grid if your card is used in the [sections view](https://www.home-assistant.io/dashboards/sections/). Each section is divided in 12 columns.
If you don't define this method, the card will take 12 columns and will ignore the rows of the grid.

A cell of the grid is defined with the following dimension:

* width: width of the section divided by 12 (approximately `30px`)
* height: `56px`
* gap between cells: `8px`

The different grid options are:

* `rows`: Default number of rows the card takes. Do not define this value if you want your card to ignore the rows of the grid (not defined by default)
* `min_rows`: Minimal number of rows the card takes (`1` by default)
* `max_rows`: Maximal number of rows the card takes (not defined by default)
* `columns`: Default number of columns the card takes. Set it to `full` to enforce your card to be full width, (`12` by default)
* `min_columns`: Minimal number of columns the card takes (`1` by default)
* `max_columns`: Maximal number of columns the card takes (not defined by default)

For the number of columns, it's `highly` recommended to use multiple of 3 for the default value (`3`, `6`, `9` or `12`) so your card will have better looking on the dashboard by default.

Example of implementation:

```
public getGridOptions() {
  return {
    rows: 2,
    columns: 6,
    min_rows: 2,
  };
}
```

In this example, the card will take 6 x 2 cells by default. The height of the card cannot be smaller than 2 rows. According to the cell dimension, the card will have a height of `120px` (`2` \* `56px` + `8px`).

## Advanced example

Resources to load in dashboards are imported as a JS module import. Below is an example of a custom card using JS modules that does all the fancy things.

![Screenshot of the wired card](data:image/png;base64,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)

Create a new file in your Home Assistant config dir as `<config>/www/wired-cards.js` and put in the following contents:

```
import "https://unpkg.com/[email protected]/wired-card.js?module";
import "https://unpkg.com/[email protected]/wired-toggle.js?module";
import {
  LitElement,
  html,
  css,
} from "https://unpkg.com/[email protected]/lit-element.js?module";

function loadCSS(url) {
  const link = document.createElement("link");
  link.type = "text/css";
  link.rel = "stylesheet";
  link.href = url;
  document.head.appendChild(link);
}

loadCSS("https://fonts.googleapis.com/css?family=Gloria+Hallelujah");

class WiredToggleCard extends LitElement {
  static get properties() {
    return {
      hass: {},
      config: {},
    };
  }

  render() {
    return html`
      <wired-card elevation="2">
        ${this.config.entities.map((ent) => {
          const stateObj = this.hass.states[ent];
          return stateObj
            ? html`
                <div class="state">
                  ${stateObj.attributes.friendly_name}
                  <wired-toggle
                    .checked="${stateObj.state === "on"}"
                    @change="${(ev) => this._toggle(stateObj)}"
                  ></wired-toggle>
                </div>
              `
            : html` <div class="not-found">Entity ${ent} not found.</div> `;
        })}
      </wired-card>
    `;
  }

  setConfig(config) {
    if (!config.entities) {
      throw new Error("You need to define entities");
    }
    this.config = config;
  }

  // The height of your card. Home Assistant uses this to automatically
  // distribute all cards over the available columns.
  getCardSize() {
    return this.config.entities.length + 1;
  }

  _toggle(state) {
    this.hass.callService("homeassistant", "toggle", {
      entity_id: state.entity_id,
    });
  }

  static get styles() {
    return css`
      :host {
        font-family: "Gloria Hallelujah", cursive;
      }
      wired-card {
        background-color: white;
        padding: 16px;
        display: block;
        font-size: 18px;
      }
      .state {
        display: flex;
        justify-content: space-between;
        padding: 8px;
        align-items: center;
      }
      .not-found {
        background-color: yellow;
        font-family: sans-serif;
        font-size: 14px;
        padding: 8px;
      }
      wired-toggle {
        margin-left: 8px;
      }
    `;
  }
}
customElements.define("wired-toggle-card", WiredToggleCard);
```

Add a resource to your dashboard config with URL `/local/wired-cards.js` and type `module`.

And for your configuration:

```
# Example dashboard configuration
views:
  - name: Example
    cards:
      - type: "custom:wired-toggle-card"
        entities:
          - input_boolean.switch_ac_kitchen
          - input_boolean.switch_ac_livingroom
          - input_boolean.switch_tv
```

## Graphical card configuration

Your card can define a `getConfigElement` method that returns a custom element for editing the user configuration. Home Assistant will display this element in the card editor in the dashboard.

Your card can also define a `getStubConfig` method that returns a default card configuration (without the `type:` parameter) in json form for use by the card type picker in the dashboard.

Home Assistant will call the `setConfig` method of the config element on setup.
Home Assistant will update the `hass` property of the config element on state changes, and the `lovelace` element, which contains information about the dashboard configuration.

Changes to the configuration are communicated back to the dashboard by dispatching a `config-changed` event with the new configuration in its detail.

To have your card displayed in the card picker dialog in the dashboard, add an object describing it to the array `window.customCards`. Required properties of the object are `type` and `name` (see example below).

```
class ContentCardExample extends HTMLElement {
  static getConfigElement() {
    return document.createElement("content-card-editor");
  }

  static getStubConfig() {
    return { entity: "sun.sun" }
  }

  ...
}

customElements.define('content-card-example', ContentCardExample);
```

```
class ContentCardEditor extends LitElement {
  setConfig(config) {
    this._config = config;
  }

  configChanged(newConfig) {
    const event = new Event("config-changed", {
      bubbles: true,
      composed: true,
    });
    event.detail = { config: newConfig };
    this.dispatchEvent(event);
  }
}

customElements.define("content-card-editor", ContentCardEditor);
window.customCards = window.customCards || [];
window.customCards.push({
  type: "content-card-example",
  name: "Content Card",
  preview: false, // Optional - defaults to false
  description: "A custom card made by me!", // Optional
  documentationURL:
    "https://developers.home-assistant.io/docs/frontend/custom-ui/custom-card", // Adds a help link in the frontend card editor
});
```

### Using the built-in form editor

While one way to configure a graphical editor is to supply a custom editor element, another option for cards with relatively simple configuration requirements is to use the built-in frontend form editor. This is done by defining a static `getConfigForm` function in your card class, that returns a form schema defining the shape of your configuration form.

Example:

```
  static getConfigForm() {
    return {
      schema: [
        { name: "label", selector: { label: {} } },
        { name: "entity", required: true, selector: { entity: {} } },
        {
          type: "grid",
          name: "",
          schema: [
            { name: "name", selector: { text: {} } },
            {
              name: "icon",
              selector: {
                icon: {},
              },
              context: {
                icon_entity: "entity",
              },
            },
            {
              name: "attribute",
              selector: {
                attribute: {},
              },
              context: {
                filter_entity: "entity",
              },
            },
            { name: "unit", selector: { text: {} } },
            { name: "theme", selector: { theme: {} } },
            { name: "state_color", selector: { boolean: {} } },
          ],
        },
      ],
      computeLabel: (schema) => {
        if (schema.name === "icon") return "Special Icon";
        return undefined;
      },
      computeHelper: (schema) => {
        switch (schema.name) {
          case "entity":
            return "This text describes the function of the entity selector";
          case "unit":
            return "The unit of measurement for this card";
        }
        return undefined;
      },
      assertConfig: (config) => {
        if (config.other_option) {
          throw new Error("'other_option' is unexpected.");
        }
      },
    };
  }
```

From this function, you should return an object with up to 4 keys:

* `schema` *(required)*: This is a list of schema objects, one per form field, defining various properties of the field, like the name and selector.
* `computeLabel` *(optional)*: This callback function will be called per form field, allowing the card to define the label that will be displayed for the field. If `undefined`, Home Assistant may apply a known translation for generic field names like `entity`, or you can supply your own translations.
* `computeHelper` *(optional)*: This callback function will be called per form field, allowing you to define longer helper text for the field, which will be displayed below the field.
* `assertConfig` *(optional)*: On each update of the configuration, the user's config will be passed to this callback function. If you throw an `Error` during this callback, the visual editor will be disabled. This can be used to disable the visual editor when the user enters incompatible data, like entering an object in yaml for a selector that expects a string. If a subsequent execution of this callback does not throw an error, the visual editor will be re-enabled.

This example then results in the following config form:
![Screenshot of the config form](/assets/images/dashboard-custom-card-config-form-981e1bf156ad8d83b75e9e65b739829c.png)

#### Form Schema Elements

The form schema can have individual controls, grids, or expansion panels, configured with the following options:

Controls:

* `name` *(required)*: The name of the control.
* `selector` *(optional)*: The selector configuration for this control (see [selectors](https://www.home-assistant.io/docs/blueprint/selectors/) for available options)
* `type` *(optional)*: If selector is not defined, there are native form types like `float` and `boolean`, though using selectors is preferred.

Grids:

* `type` *(required)*: `grid`
* `name` *(required)*: Key for this grid in the form data object (see `flatten`)
* `schema` *(required)*: A list of child controls in the grid
* `flatten` *(optional)*: `true`/`false` if child control data should be flattened into the main data dictionary, or under a sub-dictionary with the name of this grid
* `column_min_width` *(optional)*: CSS property for the minimum width of the cells in the grid (e.g. `200px`)

Expansion Panel:

* `type` *(required)*: `expandable`
* `name` *(required)*: Key for this panel in the form data object (see `flatten`)
* `schema` *(required)*: A list of child controls in the expansion panel
* `title` *(optional)*: A heading on the panel
* `flatten` *(optional)*: `true`/`false` if child control data should be flattened into the main data dictionary, or under a sub-dictionary with the name of this panel

This is not an exhaustive list of all options, more configuration options are listed at [ha-form/types.ts](https://github.com/home-assistant/frontend/blob/master/src/components/ha-form/types.ts)