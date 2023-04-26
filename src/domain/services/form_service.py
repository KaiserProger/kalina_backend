from uuid import UUID
from app.domain.entities.task import Task
from app.domain.entities.form import Form
from app.domain.interfaces.form_repository import FormRepositoryProto
from app.domain.interfaces.form_service import FormServiceProto
from app.schemas.form import FormDTO
from app.schemas.task import TaskDTO


class FormService(FormServiceProto):
    def __init__(self, form_repo: FormRepositoryProto):
        self.form_repo = form_repo

    async def create_template(self, tasks: list[TaskDTO], name: str):
        form = Form(name=name, is_template=True)  # type: ignore
        for task in tasks:
            form.tasks.append(Task(task_content=task.task_content,
                                   task_type=task.task_type,
                                   answers=task.answer))  # type: ignore
        await self.form_repo.create(form)

    async def get_templates(self):
        templates = await self.form_repo.get_templates()
        return list(map(lambda model: FormDTO.from_orm(model), templates))

    async def get_template(self, template_id: UUID):
        return FormDTO.from_orm(await self.form_repo.read_by_id(template_id))
