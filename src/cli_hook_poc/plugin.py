from kedro.framework.cli.hooks import cli_hook_impl
from kedro.framework.hooks import hook_impl


class CombineHook:
    @cli_hook_impl
    def before_command_run(self):
        print("****POC*****: before_cli_command")
        print(id(self))

    @hook_impl
    def after_catalog_created(self):
        print("****POC*****: after_catalog_created")
        print(id(self))


# project_hooks = CombineHook()
hook = CombineHook()