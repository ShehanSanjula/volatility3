from volatility3.framework import interfaces, constants


class KernelModule(interfaces.automagic.AutomagicInterface):
    """Finds ModuleRequirements and ensures their layer, symbols and offsets"""

    def __call__(self,
                 context: interfaces.context.ContextInterface,
                 config_path: str,
                 requirement: interfaces.configuration.RequirementInterface,
                 progress_callback: constants.ProgressCallback = None) -> None:
        if requirement.unsatisfied(context, config_path):
            pass
