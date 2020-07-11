from waitress import serve
from aicup_results import create_app
serve(create_app(), listen='*:80')