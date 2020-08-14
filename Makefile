
test-nlu:
	rm -f -r NLU_results/*
	rasa test nlu --config NLU_pipelines --cross-validation --out NLU_results --runs 3 --percentages 0 --quiet
test-core:
	rm -f -r CORE_models/*
	rasa train core -c $(wildcard CORE_policies/*) --stories data/stories.md --out CORE_models --runs 1 --percentages 0 --quiet
	rm -f -r CORE_results/*
	rasa test core -m CORE_models --evaluate-model-directory --stories data/stories.md --out CORE_results
test-e2e:
	rm -f -r END2END_models/*
	rm -f -r END2END_results/*
	$(foreach file, $(wildcard END2END_configs/*), \
		rasa train --config $(file) --quiet --out END2END_models/$(basename $(notdir $(file))); \
		python3 test_e2e.py $(basename $(notdir $(file))); )
