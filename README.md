# Action Bump Version

[![actions-workflow-lint][actions-workflow-lint-badge]][actions-workflow-lint]
[![release][release-badge]][release]
[![license][license-badge]][license]

This is a GitHub Action to Bump Version for Calaos Packages.

## Inputs

|          NAME          |                                                  DESCRIPTION                                                  |   TYPE   | REQUIRED | DEFAULT       |
|------------------------|---------------------------------------------------------------------------------------------------------------|----------|----------|---------------|
| `version_fragment`     | The part to bump. Possible options are [ major / minor / patch / prerelease ]                                 | `string` | `true`   | `prerelease`  |

## Outputs

| NAME             |                                            DESCRIPTION                                             |   TYPE   |
|------------------|----------------------------------------------------------------------------------------------------|----------|
| `version_bumped` | The bumped version string                                                                          | `string` |

## License

Copyright 2023 Calaos Team.

Action Bump Version is released under the [Apache License 2.0](./LICENSE).
