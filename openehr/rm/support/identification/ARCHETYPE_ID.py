__author__ = 'chrispess'


''' léxico
archetype_id: qualified_rm_entity ‘.’ domain_concept ‘.’ version_id
qualified_rm_entity: rm_originator ‘-’ rm_name ‘-’ rm_entity
rm_originator: V_ALPHANUMERIC_NAME
rm_name: V_ALPHANUMERIC_NAME
rm_entity: V_ALPHANUMERIC_NAME
domain_concept: concept_name { ‘-’ specialisation }*
concept_name: V_ALPHANUMERIC_NAME
specialisation: V_ALPHANUMERIC_NAME
version_id: ‘v’ V_NONZERO_DIGIT [ V_NUMBER ]
# padrão léxico
V_ALPHANUMERIC_NAME: [a-zA-Z][a-zA-Z0-9_]+
V_NONZERO_DIGIT: [1-9]
V_NUMBER: [0-9]+   '''



from openehr.rm.support.identification import OBJECT_ID

class ARCHETYPE_ID(OBJECT_ID):

    #referência, globalmente, uma entidade do modelo.
    # ex openehr-composition-OBSERVATION
    qualifiedRmEntity = str()

    #organizaão de onde se origina o modelo de referência base do arquétipo.
    #ex: "openehr", "cen", "hl7"
    rmOriginator = str()

    #nome do modelo de referência.
    # ex: "en13606", "ehr_rm"
    rmName = str()

    #nome do nível ontológico do modelo de referência do qual o arquétipo se origina.
    # ex: "section", "entry", "folder", "composition"
    rmEntity = str()

    #nomedoconceito representado pelo arquétipo, incluindo especializações.
    # ex: "biochemistry_result-cholesterol"
    domainConcept = str()

    #nome da especialização do conceito, se o arquétipo for a especialização
    # de outro arquétipo. ex: "cholesterol"
    specialization = str()

    #versão do arquétipo
    versionID = str()


    def __init__(self, rm_originator, rm_name, rm_entity, domain_concept, specialization, version_id):
        self.rmOriginator = rm_originator







