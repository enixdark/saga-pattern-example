import json
import os

from kafka import KafkaProducer

from src.library.logger.Logger import Logger


class BartenderDao:

    def __init__(self):
        self.__producer = KafkaProducer(
            bootstrap_servers=[os.getenv("KAKFA_SERVER")],
            value_serializer=lambda v: json.dumps(v).encode("utf-8")
        )
        self.__food_topic = os.getenv("KAKFA_TOPIC_DRINK")

    def publish(self, items):
        for item in items:
            Logger.info(f"publishing to drink_topic: {item}")
            self.__producer.send(
                topic=self.__food_topic,
                value=item
            )