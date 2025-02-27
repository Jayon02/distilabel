# Copyright 2023-present, Argilla, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from distilabel.models.llms import vLLM

if __name__ == "__main__":
    llm = vLLM(
        model="prometheus-eval/prometheus-7b-v2.0",
        chat_template="[INST] {{ messages[0]['content']}} [/INST]",
    )

    llm.load()
    # Call the model
    output = llm.generate_outputs(
        inputs=[[{"role": "user", "content": "Hello world!"}]]
    )

    print(output)
