This example shows how you can set an expected value in vars.csv or vars.json and emit a PASS/FAIL based on it:

```
modsys eval --prompts prompts.txt --vars vars.csv --providers google_perspective:analyze --output output.json
```
