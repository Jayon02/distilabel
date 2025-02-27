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

from pydantic import BaseModel

from distilabel.models.llms import SGLang

if __name__ == "__main__":

    class User(BaseModel):
        name: str
        last_name: str
        id: int

    llm = SGLang(
        model="Qwen/Qwen2.5-Coder-3B-Instruct",
        structured_output={"format": "json", "schema": User},
    )
    llm.load()
    # Call the model
    output = llm.generate_outputs(
        inputs=[
            [
                {
                    "role": "user",
                    "content": "Create a user profile for the following marathon",
                }
            ]
        ]
    )
    print(output)
