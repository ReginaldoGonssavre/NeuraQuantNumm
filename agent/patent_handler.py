import logging

class PatentHandler:
    """Agente responsável pelo gerenciamento simulado de patentes."""
    def __init__(self):
        self.patents_filed = []
        logging.info("PatentHandler inicializado.")

    def file_patent(self, research_results):
        """Simula o processo de submissão de uma patente.

        Args:
            research_results (dict): Resultados da pesquisa a serem patenteados.

        Returns:
            str: Status da submissão da patente.
        """
        patent_id = f"PAT-{len(self.patents_filed) + 1:04d}"
        self.patents_filed.append({"id": patent_id, "results": research_results, "status": "pending"})
        logging.info(f"Patente {patent_id} submetida com resultados: {research_results}")
        return f"Patente {patent_id} submetida com sucesso (status: pending)."

    def check_status(self, patent_id):
        """Verifica o status de uma patente simulada."
        for patent in self.patents_filed:
            if patent["id"] == patent_id:
                return patent["status"]
        return "Patente não encontrada."
