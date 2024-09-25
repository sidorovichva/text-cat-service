

class VectorizationService:

    @classmethod
    def vectorize(cls, text: str) -> list[str]:
        return text.split(" ")
