# Documentação

## Executar no localhost

```shell
$ uv run uvicorn main:app --reload
```

## Executar no Render

```shell
$ uv run uvicorn main:app --host 0.0.0.0 --port 10000

OU

$ uv run uvicorn main:app --host 0.0.0.0 --port $PORT
```

URL: `https://helix-ws-test.onrender.com/`

## Repositório no GitHub

`https://github.com/lossurdo/helix-ws-test`