"""Centralized repository of Application Commands/Task Names for communication between bounded contexts.

Moving this to the Application layer ensures the Domain and Application layers
remain independent of Infrastructure details (Clean Architecture Dependency Rule).
"""

class TaskNames:
    """Task Constants mapping explicitly to Bounded Context Use Cases."""
    SYNC_B3_COMPANIES = "run_sync_b3_companies"
