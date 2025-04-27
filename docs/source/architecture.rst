System Architecture
===================

Core Components
---------------
.. graphviz::

   digraph architecture {
      rankdir=LR;
      node [shape=box];
      
      User -> Main;
      Main -> OpenAI_Handler;
      Main -> Template_Manager;
      Main -> PDF_Generator;
      Template_Manager -> PDF_Generator;
      OpenAI_Handler -> PDF_Generator;
   }

Data Flow
---------
1. User input through CLI
2. Template configuration loading
3. AI processing via OpenAI API
4. Markdown to PDF conversion
5. Output generation