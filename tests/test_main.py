from pytest_mock import MockerFixture
from pathlib import Path
import subprocess
from create_tetra_wrapper import parser, main


def test_main(mocker: MockerFixture, tmp_path: Path):
    """
    Running main w/o options should create a unit sphere.
    """
    outputdir = tmp_path / 'outgoing'
    output_file = outputdir / 'sphere_81920.obj'

    options = parser.parse_args([])
    spy = mocker.spy(subprocess, 'run')
    main(options, outputdir)
    assert output_file.exists()
    spy.assert_called_once()
    assert spy.call_args[0][0][0] == 'create_tetra'
