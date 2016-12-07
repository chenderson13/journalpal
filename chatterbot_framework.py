# -*- coding: utf-8 -*-

from chatterbot import ChatBot
import logging

logging.basicConfig(level=logging.INFO)

bot = ChatBot(
    "JournalPal",
    storage_adapter="chatterbot.adapters.storage.MongoDatabaseAdapter",
    input_adapter="chatterbot.adapters.input.TerminalAdapter",
    output_adapter="chatterbot.adapters.output.TerminalAdapter",
    logic_adapters=[
    	"chatterbot.adapters.logic.ClosestMatchAdapter",
    	"chatterbot.adapters.logic.ClosestMeaningAdapter",
        "chatterbot.adapters.logic.MathematicalEvaluation",
        "chatterbot.adapters.logic.TimeLogicAdapter"
    ],
    filters=['chatterbot.filters.RepetitiveResponseFilter'],
    database="database_1"
)


print 'Welcome to JournalPal!\n JournalPal gives you a space to reflect on your experiences. Unlike a traditional journal, JournalPal understands what youre writing about and can give you writing prompts and feedback.\n\n Try writing your first entry!\n-'
 
while True:
    try:
     bot_input = bot.get_response(None)

    except(KeyboardInterrupt, EOFError, SystemExit):
        break

