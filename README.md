# marioai-2009
Original source code from http://julian.togelius.com/mariocompetition2009/index.php

## Run
### Manual
```sh
java -classpath classes ch.idsia.scenarios.Play
```
or

```sh
ant play
```

### Using Agent
```sh
java -classpath classes ch.idsia.scenarios.Play ch.idsia.ai.agents.ai.ForwardAgent
```

### Client / Server Control via TCP
Sever

```sh
java -classpath classes ch.idsia.scenarios.MainRun -server on
```
Client

```sh
python src/python/competition/ipymario.py
```

Run the following setup if necessary.

```sh
virtualenv env #Use Python 2.7
source env/bin/activate
pip install -r requirements.txt
```