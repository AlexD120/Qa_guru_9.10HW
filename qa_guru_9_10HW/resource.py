from pathlib import Path


def path(image_name):
    return str(Path(__file__).parent.joinpath(f'qa_guru_9_10HW/image/{image_name}'))
