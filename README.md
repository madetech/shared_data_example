# FastAPI

experimenting with fastapi

## ENV
create a `.env` file in the main directory

you will need to add:
```SECRET_IDENTITY='<secret stuff>'```

I literally used it to show you can hide whatever you like in there.

## RUN

Make sure you have docker desktop up and running.
```bash
$ docker compose up --build
```

then click the linked location that fets shown in the terminal.

## WORKING ON THE CODE
Create a virtual environment
```bash
$ python3 -m venv .venv
```

source the virtual environment:
```bash
$ . ./.venv/bin/activate
```
install the requirements:
```bash
$ pip install -r requirements.txt
```
That should be enough to get it all working

You can run it without docker using:
```bash
$ uvicorn main:app --reload
```

The 'reload' flag is only needed if you want it to load changes as you make it.

## TESTED
* docker environment working
* env working

