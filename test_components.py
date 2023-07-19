from xai_components.base import InArg, OutArg, InCompArg, Component, xai_component, secret, chat

@xai_component
class AllLiteralTypes(Component):
    string_port: InArg[str]
    int_port: InArg[int]
    float_port: InArg[float]
    boolean_port: InArg[bool]
    list_port: InArg[list]
    tuple_port: InArg[tuple]
    dict_port: InArg[dict]
    secret_port: InArg[secret]
    chat_port: InArg[chat]
    any_port: InArg[any]

    def execute(self, ctx) -> None:
        data_types = {
            "String inPort": self.string_port.value,
            "Integer inPort": self.int_port.value,
            "Float inPort": self.float_port.value,
            "Boolean inPort": self.boolean_port.value,
            "List inPort": self.list_port.value,
            "Tuple inPort": self.tuple_port.value,
            "Dict inPort": self.dict_port.value,
            "Secret inPort": self.secret_port.value,
            "Chat inPort": self.chat_port.value,
            "Any inPort": self.any_port.value
        }

        for data_type, value in data_types.items():
            print(data_type + ":")
            print(value)