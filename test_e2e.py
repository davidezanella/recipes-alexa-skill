import asyncio
import json
import sys
from typing import Text, Dict, Optional, List, Any, Iterable, Tuple, Union

import rasa.utils.io as io_utils
from rasa.constants import (
    DEFAULT_RESULTS_PATH,
)
import rasa.cli.utils as cli_utils
import rasa.utils.common as utils
from rasa.exceptions import ModelNotFound


def test_core(
    model: Optional[Text] = None,
    stories: Optional[Text] = None,
    endpoints: Optional[Text] = None,
    output: Text = DEFAULT_RESULTS_PATH
):
    import rasa.core.utils as core_utils
    import rasa.model
    from rasa.core.interpreter import RegexInterpreter, NaturalLanguageInterpreter
    from rasa.core.agent import Agent

    _endpoints = core_utils.AvailableEndpoints.read_endpoints(endpoints)

    additional_arguments = {'e2e': True}

    if output:
        io_utils.create_directory(output)

    try:
        unpacked_model = rasa.model.get_model(model)
    except ModelNotFound:
        cli_utils.print_error(
            "Unable to test: could not find a model. Use 'rasa train' to train a "
            "Rasa model and provide it via the '--model' argument."
        )
        return

    core_path, nlu_path = rasa.model.get_model_subdirectories(unpacked_model)

    if not core_path:
        cli_utils.print_error(
            "Unable to test: could not find a Core model. Use 'rasa train' to train a "
            "Rasa model and provide it via the '--model' argument."
        )

    use_e2e = additional_arguments.get("e2e", False)

    _interpreter = RegexInterpreter()
    if nlu_path:
        _interpreter = NaturalLanguageInterpreter.create(_endpoints.nlu or nlu_path)
    elif use_e2e:
        cli_utils.print_warning(
            "No NLU model found. Using default 'RegexInterpreter' for end-to-end "
            "evaluation."
        )

    _agent = Agent.load(unpacked_model, interpreter=_interpreter)

    from rasa.core.test import test

    kwargs = utils.minimal_kwargs(additional_arguments, test, ["stories", "agent"])

    _test_core(stories, _agent, output, **kwargs)


def _test_core(
    stories: Optional[Text], agent: "Agent", output_directory: Text, **kwargs: Any
) -> None:
    from rasa.core.test import test

    loop = asyncio.get_event_loop()
    res = loop.run_until_complete(
        test(stories, agent, out_directory=output_directory, **kwargs)
    )

    print(res['report'])

    with open(output_directory + '/results.json', 'w') as outfile:
        json.dump(res, outfile, ensure_ascii=True, indent=4)


config = sys.argv[1]
test_core('END2END_models/' + config, 'tests', None, 'END2END_results/' + config)
