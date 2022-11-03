from .administrador_admin import AdministradorAdmin
from .aluno_admin import AlunoAdmin
from .curso_admin import CursoAdmin
from .disciplina_inline import DisciplinaInline
from .periodo_admin import PeriodoAdmin
from .professor_admin import ProfessorAdmin
from .registro_admin import RegistroAdmin
from .registro_inline import RegistroInline
from .turma_admin import TurmaAdmin
from .vinculo_admin import VinculoAdmin


__all__ = [
    AdministradorAdmin,
    AlunoAdmin,
    CursoAdmin,
    DisciplinaInline,
    PeriodoAdmin,
    ProfessorAdmin,
    RegistroAdmin,
    RegistroInline,
    TurmaAdmin,
    VinculoAdmin,
]