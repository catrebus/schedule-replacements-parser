from bot.crud import get_users


async def announce_new_replacements(pdfData) -> None:
    from bot.main import bot
    """Рассылка замен всем пользователям"""
    replacements = pdfData.replacements

    if len(replacements) == 0:
        return

    users = await get_users()
    for replacement in replacements:
        # Формирование сообщения
        replacement = replacement.model_dump()
        message = f'🔔ЗАМЕНА!\nДата: {replacement['date']}\nГруппа: {replacement['group']}\nЧто поменялось: {', '.join(replacement['changeType'])}.\n\n'
        before = f'✖️БЫЛО\nПреподаватель: {replacement['teacherBefore']}\nНомер пары: {replacement["pairNumberBefore"]}\nПредмет: {replacement["disciplineBefore"]}\nКабинет: {replacement["classBefore"]}\n\n'
        after = f'✔️СТАЛО\nПреподаватель: {replacement['teacherNow']}\nНомер пары: {replacement["pairNumberNow"]}\nПредмет: {replacement["disciplineNow"]}\nКабинет: {replacement["classNow"]}\n\n'
        if replacement['changeType'] == ['отмена занятия']:
            message += before
        elif replacement['changeType'] == ['добавление занятия']:
            message += after
        else:
            message += before
            message += after

        # Рассылка всем пользователям
        for user in users:
            try:
                await bot.send_message(user, message)
            except Exception:
                pass
    print('Replacements announced successfully')