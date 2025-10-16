from models import get_factory, Document

def process_documents(factory, doc_types):
    for doc_type in doc_types:
        try:
            doc = factory.create(doc_type)
            print(doc.render())
        except ValueError as e:
            print(f"Error: {e}")

doc_types = ["report", "invoice", "contract"]

print("\nCorp Режим")
corp_factory = get_factory("corp")
process_documents(corp_factory, doc_types)

print("\nShadow Режим")
shadow_factory = get_factory("shadow")
process_documents(shadow_factory, doc_types)