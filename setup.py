#   Copyright 2021 Evan Bolyen
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

from setuptools import setup, find_packages


setup(
    name="q2-enrich",
    version='0.0.1.dev',
    packages=find_packages(),
    package_data={},
    author="Annabelle Brown",
    author_email="annabelle811@live.com",
    description="Generate reveal.js presentations with collation",
    license='Apache-2.0',
    url="https://github.com/Annabelle-Brown/q2-enrich.git",
    # This entry_point defines a structure in your site-packages which
    # pkg_resources can use to load "stuff" from a "namespace".
    # QIIME 2 has defined a namespace called qiime2.plugins, and it should
    # have look like <project_name>=<module path>:<reference>
    # A package _could_ have multiple plugins, but it would be unusual.
    entry_points={
        'qiime2.plugins': ['q2-enrich=q2_enrich.plugin_setup:plugin']
    },
    zip_safe=False,
)
