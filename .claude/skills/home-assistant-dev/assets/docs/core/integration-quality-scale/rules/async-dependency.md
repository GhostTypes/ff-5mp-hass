# Source: https://developers.home-assistant.io/docs/core/integration-quality-scale/rules/async-dependency

## Reasoning

Home Assistant works with asyncio to be efficient when handling tasks.
To avoid switching context between the asyncio event loop and other threads, which is costly performance wise, ideally, your library should also use asyncio.

This results not only in a more efficient system but the code is also more neat.

## Additional resources

More information on how to create a library can be found in the [documentation](/docs/api_lib_index).

## Exceptions

There are no exceptions to this rule.

## Related rules

* [inject-websession](/docs/core/integration-quality-scale/rules/inject-websession): The integration dependency supports passing in a websession