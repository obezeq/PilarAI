Contributing Guide
==================

Development Setup
-----------------
.. code-block:: bash

   # Install development dependencies
   pip install -r requirements-dev.txt
   
   # Run tests
   pytest tests/ --cov=src --cov-report=html

Coding Standards
----------------
- PEP 8 compliance
- Google-style docstrings
- Type hints for all public methods
- 80% test coverage minimum

Release Process
---------------
1. Update version in `__version__.py`
2. Update CHANGELOG.md
3. Create signed tag
4. Push to main branch
5. GitHub Actions deploys package