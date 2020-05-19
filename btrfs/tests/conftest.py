# (C) Datadog, Inc. 2020-present
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)

import pytest


@pytest.fixture(scope="session")
def dd_environment():
    yield {'instances': [{}]}
