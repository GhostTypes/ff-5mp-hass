# Source: https://developers.home-assistant.io/docs/architecture_index

Home Assistant provides a platform for home control and home automation. Home Assistant is not just an application: it's an embedded system that provides an experience like other consumer off-the-shelf products: onboarding, configuration and updating is all done via an easy to use interface.

* The [operating system](/docs/operating-system) provides the bare minimal Linux environment to run Supervisor and Core.
* The [Supervisor](/docs/supervisor) manages the operating system.
* The [Core](/docs/architecture/core) interacts with the user, the supervisor and IoT devices & services.

![Full picture of Home Assistant](/img/en/architecture/full.svg)

## Running parts of the stack

Users have different requirements for what they want from a home automation platform. That's why it is possible to run only part of the Home Assistant stack. For more information, see the [installation instructions](https://www.home-assistant.io/installation/).