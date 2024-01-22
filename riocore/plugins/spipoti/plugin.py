from riocore.plugins import PluginBase


class Plugin(PluginBase):
    def setup(self):
        self.NAME = "spipoti"
        self.VERILOGS = ["spipoti.v"]
        self.PINDEFAULTS = {
            "mosi": {
                "direction": "output",
                "invert": False,
                "pullup": False,
            },
            "sclk": {
                "direction": "output",
                "invert": False,
                "pullup": False,
            },
            "sel": {
                "direction": "output",
                "invert": False,
                "pullup": False,
            },
        }
        self.INTERFACE = {
            "value": {
                "size": 8,
                "direction": "output",
            },
        }
        self.SIGNALS = {
            "value": {
                "direction": "output",
            },
        }
        self.INFO = "spi analog-poti"
        self.DESCRIPTION = ""

    def gateware_instances(self):
        instances = self.gateware_instances_base()
        instance = instances[self.instances_name]
        instance_predefines = instance["predefines"]
        instance_parameter = instance["parameter"]
        instance_arguments = instance["arguments"]
        instance_parameter["WIDTH"] = self.plugin_setup.get("width", "8")
        frequency = int(self.plugin_setup.get("frequency", 1000))
        divider = self.system_setup["speed"] // frequency
        instance_parameter["DIVIDER"] = divider
        return instances
