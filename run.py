from librasic import app
from librasic.modules.app_setup import (
    setup_app_config,
    setup_app_db,
    setup_app_env_vars,
)

if __name__ == "__main__":
    setup_app_config()
    setup_app_db()
    setup_app_env_vars()

    app.run(use_reloader=True, debug=True, port=7134)
