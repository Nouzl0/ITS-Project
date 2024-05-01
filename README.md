# ITS-Projekt BDD-Testy-OpenCart

Implemente regresních testů pro webovou aplikaci OpenCart pomocou technologií Docker, Python, Selenium, Behave. Testovány byly pouze základní funkce aplikace OpenCart. 


- **Autor:** Nikolas Nosál, <xnosal01@stud.fit.vutbr.cz>
- **Report:** [BugReport](report.pdf)

## Matice pokrytí artefaktů

Čísla testů jednoznačně identifikují scénář v souborech `.feature`.

| Page                          | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 | 24 |
|-------------------------------|---|---|---|---|---|---|---|---|---|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|
| Home                          | x |   |   |   |   |   |   |   |   |    | x  |    |    |    |    |    |    |    |    |    |    |    |    |    |
| (Panel) User Navigation       |   |   |   | x |   |   |   |   |   |    | x  |    |    |    |    |    |    |    |    |    |    |    |    |    |
| (Panel) Cart Preview          |   |   | x |   |   |   |   | x | x |    |    |    |    | x  | x  | x  |    |    |    |    |    |    |    |    |
| Product Details               | x | x | x |   |   |   |   |   |   |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |
| Search Results                |   |   |   | x | x | x |   |   |   |    | x  | x  |    |    |    |    |    |    |    |    |    |    |    |    |
| Comparison                    |   |   |   |   |   |   | x | x |   |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |
| Wish List                     |   |   |   |   |   |   |   |   |   |    |    |    | x  | x  |    |    |    |    |    |    |    |    |    |    |
| Checkout                      |   |   |   |   |   |   |   |   | x | x  |    |    |    |    |    |    |    |    |    |    |    |    |    |    |
| Cart                          |   |   |   |   |   |   |   |   |   |    |    |    |    |    | x  | x  |    |    |    |    |    |    |    |    |
| (Panel) Catalog Menu          |   |   |   |   |   |   |   |   |   |    |    |    |    |    |    |    | x  |    |    |    |    |    |    |    |
| Categories                    |   |   |   |   |   |   |   |   |   |    |    |    |    |    |    |    |    | x  |    | x  |    |    |    |    |
| Category Edit                 |   |   |   |   |   |   |   |   |   |    |    |    |    |    |    |    |    |    | x  |    |    |    |    |    |
| Products                      |   |   |   |   |   |   |   |   |   |    |    |    |    |    |    |    |    |    |    |    | x  |    |    |    |
| Product Edit                  |   |   |   |   |   |   |   |   |   |    |    |    |    |    |    |    |    |    |    |    |    | x  | x  |    |
| Product Add                   |   |   |   |   |   |   |   |   |   |    |    |    |    |    |    |    |    |    |    |    |    |    |    | x  |


## Matice pokrytí aktivit

| Activities                | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 | 24 | 
|---------------------------|---|---|---|---|---|---|---|---|---|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|
| Searching for products    |   |   |   | x | x | x |   |   |   |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |
| Searching categories      |   |   |   |   |   |   |   |   |   |    | x  | x  |    |    |    |    |    |    |    |    |    |    |    |    |
| Checking product          | x | x |   |   |   |   |   |   |   |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    | 
| Comparing products        |   |   |   |   |   | x | x | x |   |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    | 
| Using the cart            |   |   | x |   |   |   |   | x |   |    |    |    |    | x  | x  | x  |    |    |    |    |    |    |    |    | 
| Using wish list           |   |   |   |   |   |   |   |   |   |    |    | x  | x  | x  |    |    |    |    |    |    |    |    |    |    |
| Purchasing products       |   |   |   |   |   |   |   |   | x | x  |    |    |    |    |    |    |    |    |    |    |    |    |    |    |
| Using Catalog             |   |   |   |   |   |   |   |   |   |    |    |    |    |    |    |    | x  | x  |    |    | x  |    | x  |    |
| Editing category info     |   |   |   |   |   |   |   |   |   |    |    |    |    |    |    |    |    | x  | x  |    |    |    |    |    |
| Deleting categories       |   |   |   |   |   |   |   |   |   |    |    |    |    |    |    |    |    |    |    | x  |    |    |    |    |
| Editing product data      |   |   |   |   |   |   |   |   |   |    |    |    |    |    |    |    |    |    |    |    | x  | x  |    |    |
| Adding products           |   |   |   |   |   |   |   |   |   |    |    |    |    |    |    |    |    |    |    |    |    |    | x  | x  |


## Matice Feature-Test

| Feature file                           | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 | 24 | 
|----------------------------------------|---|---|---|---|---|---|---|---|---|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|
| product_search_and_purchase.feature    | x | x | x | x | x | x | x | x | x | x  |    |    |    |    |    |    |    |    |    |    |    |    |    |    |
| wish_list_and_cart_management.feature  |   |   |   |   |   |   |   |   |   |    | x  | x  | x  | x  | x  | x  |    |    |    |    |    |    |    |    |  
| catalog_and_product_management.feature |   |   |   |   |   |   |   |   |   |    |    |    |    |    |    |    | x  | x  | x  | x  | x  | x  | x  | x  | 
