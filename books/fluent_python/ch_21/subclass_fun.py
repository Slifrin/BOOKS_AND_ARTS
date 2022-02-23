from enum import Enum, auto



class RepositoryType(Enum):
    HG = auto()
    GIT = auto()
    SVN = auto()
    PERFORCE = auto()


class Repo():
    _registry = {t : {} for t in RepositoryType}

    def __init_subclass__(cls, scm_type=None, name=None, **kwargs):
        super().__init_subclass__(**kwargs)
        if scm_type is not None:
            cls._registry[scm_type][name] = cls


class MainHgRepo(Repo, scm_type=RepositoryType.HG, name='main'):
    pass

class GenericGitRepo(Repo, scm_type=RepositoryType.GIT):
    pass



def main():
    print('Hello main')

    hg = MainHgRepo()
    # print(dir(hg))
    print(hg._registry)

    git = GenericGitRepo()
    # print(dir(git))
    print(git._registry)


if __name__ == '__main__':
    main()
        