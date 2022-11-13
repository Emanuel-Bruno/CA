from .administrador_admin import AdministradorAdmin
from .aluno_admin import AlunoAdmin
from .bloco_salas_admin import BlocoSalasAdmin
from .curso_admin import CursoAdmin
from .disciplina_inline import DisciplinaInline
from .noticia_turma_admin import NoticiaTurmaAdmin
from .noticia_turma_inline import NoticiaTurmaInline
from .periodo_admin import PeriodoAdmin
from .professor_admin import ProfessorAdmin
from .registro_admin import RegistroAdmin
from .registro_inline import RegistroInline
from .sala_admin import SalaAdmin
from .tarefa_turma_admin import TarefaTurmaAdmin
from .tarefa_turma_inline import TarefaTurmaInline
from .turma_admin import TurmaAdmin
from .vinculo_admin import VinculoAdmin


__all__ = [
    AdministradorAdmin,
    AlunoAdmin,
    BlocoSalasAdmin,
    CursoAdmin,
    DisciplinaInline,
    NoticiaTurmaAdmin,
    NoticiaTurmaInline,
    PeriodoAdmin,
    ProfessorAdmin,
    RegistroAdmin,
    RegistroInline,
    SalaAdmin,
    TarefaTurmaAdmin,
    TarefaTurmaInline,
    TurmaAdmin,
    VinculoAdmin,
]