from pathlib import Path

class Site:
def __init(self,source,dest):
    self.source  = Path(source)
    self.dest = Path(dest)

    def create_dir(self, path):
        directory = self.dest / path.relevative_to(self.source)
        directory.mkdir(parents=True, exist_ok=True)

    def build(self)
    self.dest.mkdir(parents=True, exist_ok=True)
for path in self.source.rglob("*"):
    if path.is_dir():
        self.createdir(path)
