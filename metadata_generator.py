import os
from os.path import join
from pprint import pprint
import shutil
import urllib.request
import json
from pprint import pprint

result = []
id = 0

original_data_file = open("scripts/data/bug_id_and_branch.json", "r")
original_data = json.load(original_data_file)
original_data_file.close()


for project in original_data:
    id += 1

    metadata_link = (
        "https://github.com/bears-bugs/bears-benchmark/raw/{}/bears.json".format(
            project["bugBranch"]
        )
    )
    metadata = {}

    with urllib.request.urlopen(metadata_link) as f:
        metadata = json.load(f)
        pprint(metadata)

    result.append(
        {
            "id": id,
            "subject": "-".join(project["bugBranch"].split("-")[0:2]),
            "bug_id": project["bugBranch"],
            "bug_commit": metadata["commits"]["buggyBuild"]["sha"],
            "repository": metadata["commits"]["buggyBuild"]["repoName"],
            "branch": project["bugBranch"],
            "source_file": "",
            "source_directory": "src/main/java",
            "class_directory": "target/classes",
            "test_directory": "src/test/java",
            "test_class_directory": "target/test-classes",
            "language": "java",
            "build_script": "build_subject",
            "config_script": "config_subject",
            "clean_script": "clean_subject",
            "test_script": "test_subject",
            "bug_type": "Test Failure",
            "java_version": 8,
            "line_numbers": [],
            "dependencies": [],
            "passing_test": [],
            "failing_test": list(
                map(
                    lambda failure: failure["testClass"],
                    metadata["tests"]["failureDetails"],
                )
            ),
            "test_timeout": 5,
            "count_neg": metadata["tests"]["overallMetrics"]["numberFailing"]
            + metadata["tests"]["overallMetrics"]["numberErroring"],
            "count_pos": metadata["tests"]["overallMetrics"]["numberPassing"],
        }
    )

x = open("meta-data.json", "w")
x.write(json.dumps(result, indent=4))
x.close()
