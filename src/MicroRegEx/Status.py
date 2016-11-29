class Status:
    def __init__(self):
        self.translation = {}
        self.epsilon = []
        self.accept = False
        super().__init__()

    def __str__(self):
        return "<{} translation={} epsilon={} accept={}>".format(repr(self),
                                                                 repr(self.translation),
                                                                 repr(self.epsilon),
                                                                 repr(self.accept)
                                                                 )
