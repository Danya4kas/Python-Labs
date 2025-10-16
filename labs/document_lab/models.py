from abc import ABC, abstractmethod

class Document(ABC):
    @abstractmethod
    def render(self) -> str:
        pass

class CorporateReport(Document):
    def render(self) -> str:
        return "Corporate report"

class CorporateInvoice(Document):
    def render(self) -> str:
        return "Corporate invoice"

class CorporateContract(Document):
    def render(self) -> str:
        return "Corporate contract"

class ShadowReport(Document):
    def render(self) -> str:
        return "Shadow report"

class ShadowInvoice(Document):
    def render(self) -> str:
        return "Shadow invoice"

class ShadowContract(Document):
    def render(self) -> str:
        return "Shadow contract"

class DocumentFactory(ABC):
    @abstractmethod
    def create(self, doc_type: str) -> Document:
        pass

class CorporateDocumentFactory(DocumentFactory):
    ALLOWED_TYPES = ["report", "invoice", "contract"]

    def create(self, doc_type: str) -> Document:
        if doc_type not in self.ALLOWED_TYPES:
            raise ValueError(f"Error type: {doc_type}")
        if doc_type == "report":
            return CorporateReport()
        elif doc_type == "invoice":
            return CorporateInvoice()
        elif doc_type == "contract":
            return CorporateContract()

class ShadowDocumentFactory(DocumentFactory):
    ALLOWED_TYPES = ["report", "invoice", "contract"]

    def create(self, doc_type: str) -> Document:
        if doc_type not in self.ALLOWED_TYPES:
            raise ValueError(f"Error type: {doc_type}")
        if doc_type == "report":
            return ShadowReport()
        elif doc_type == "invoice":
            return ShadowInvoice()
        elif doc_type == "contract":
            return ShadowContract()

def get_factory(mode: str) -> DocumentFactory:
    if mode == "corp":
        return CorporateDocumentFactory()
    elif mode == "shadow":
        return ShadowDocumentFactory()
    else:
        raise ValueError(f"Unknown {mode}")