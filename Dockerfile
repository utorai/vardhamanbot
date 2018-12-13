FROM utorai/botbase

# Set work directory as xbot which is the work directory for bot base.
WORKDIR /xbot

# Copy the bot directory to the work directory.
COPY . /xbot/vardhamanbot

# Train Rasa NLU for the desired intents.
RUN pipenv run python -m rasa_nlu.train -c ./vardhamanbot/bot/config/rasa.yml --data ./vardhamanbot/bot/data/rasa.md -o models --fixed_model_name nlu --project vardhamanbot --verbose 

EXPOSE 8080

CMD pipenv run python ./vardhamanbot/bot/main.py