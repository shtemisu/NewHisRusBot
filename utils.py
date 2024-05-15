import g4f
import logging


async def generate_answer(prompt):
    try:

        response = g4f.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
        )

        return response
    except Exception as e:
        logging.error(e)

