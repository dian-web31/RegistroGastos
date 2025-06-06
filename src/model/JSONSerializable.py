from abc import ABC, abstractmethod

class JSONSerializable(ABC):
		"""
		Interfaz para objetos que pueden ser serializados en JSON.
		"""

		@abstractmethod
		def to_json(self) -> str:
				pass

		@classmethod
		@abstractmethod
		def from_json(cls, json_str: str):
				pass