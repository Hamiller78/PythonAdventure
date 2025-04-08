from enum import Enum

class TokenType(Enum):
    N = 'N'
    E = 'E'
    S = 'S'
    W = 'W'
    U = 'U'
    D = 'D'
    GO = 'GO'
    LOOK = 'LOOK'
    TAKE = 'TAKE'
    DROP = 'DROP'
    USE = 'USE'
    TALK = 'TALK'
    GIVE = 'GIVE'
    WORD = ''