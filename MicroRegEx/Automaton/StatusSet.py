import math


class StatusSet(frozenset):
    @property
    def name(self):
        # return ",".join([i.name for i in self])
        element_length = len(self)
        group_size = math.ceil(math.sqrt(element_length))

        group_string = []

        # get ascending sorted element
        element = [i.name for i in self]
        element = sorted(element, key=lambda x: int(x))
        for j in range(group_size):
            group_slice = slice(j * group_size, (j + 1) * group_size)
            element_group = element[group_slice]
            if not element_group:
                continue
            group_string.append(",".join(element_group))

        return ",\n".join(group_string)

    def __repr__(self):
        return ",".join([i.name for i in self])

    @property
    def accept(self):
        return any([sub_status.accept for sub_status in self])
