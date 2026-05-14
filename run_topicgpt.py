from topicgpt_python import *
import yaml

from topicgpt_python.log_config import get_logger

logger = get_logger()


PROVIDER = 'openai'
MODEL = 'gpt-5-mini'
# PROVIDER = 'ollama'
# MODEL = 'gemma3'

with open("context_file_config.yml", "r") as f:
    config = yaml.safe_load(f)

def run_inference():
    # logger.info("********* Started generate_topic_lvl1 *********")
    # generate_topic_lvl1(
    #     PROVIDER,
    #     MODEL,
    #     config["data_sample"],
    #     config["generation"]["prompt"],
    #     config["generation"]["seed"],
    #     config["generation"]["output"],
    #     config["generation"]["topic_output"],
    #     verbose=config["verbose"],
    # )
    # logger.info("********* Finished generate_topic_lvl1 *********")

    # Optional: Refine topics if needed
    # if config["refining_topics"]:
    #     logger.info("********* Started refine_topics *********")
    #     refine_topics(
    #         PROVIDER,
    #         MODEL,
    #         config["refinement"]["prompt"],
    #         config["generation"]["output"],
    #         config["generation"]["topic_output"],
    #         config["refinement"]["topic_output"],
    #         config["refinement"]["output"],
    #         verbose=config["verbose"],
    #         remove=config["refinement"]["remove"],
    #         mapping_file=config["refinement"]["mapping_file"]
    #     )
    #     logger.info("********* Finished refine_topics *********")

    # Assignment
    # logger.info("********* Started assign_topics *********")
    # assign_topics(
    #     PROVIDER,
    #     MODEL,
    #     config["data_sample"],
    #     config["assignment"]["prompt"],
    #     config["assignment"]["output"],
    #     config["refinement"][
    #         "topic_output"
    #     ],  # TODO: change to generation_2 if you have subtopics, or config['refinement']['topic_output'] if you refined topics
    #     verbose=config["verbose"],
    # )
    # logger.info("********* Finished assign_topics *********")

    # Correction
    logger.info("********* Started correct_topics *********")
    correct_topics(
        PROVIDER,
        MODEL,
        config["assignment"]["output"],
        config["correction"]["prompt"],
        config["refinement"][
            "topic_output"
        ],  # TODO: change to generation_2 if you have subtopics, or config['refinement']['topic_output'] if you refined topics
        config["correction"]["output"],
        verbose=config["verbose"],
    )
    logger.info("********* Finished correct_topics *********")

if __name__ == "__main__":
    run_inference()