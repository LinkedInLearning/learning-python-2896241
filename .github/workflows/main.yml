name: Copy To Branches
on:
  workflow_dispatch:
jobs:
  copy-to-branches:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
        with:
          fetch-depth: 0
      - name: Copy To Branches Action
        uses: planetoftheweb/copy-to-branches@v1
