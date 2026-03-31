from Bio.Phylo.TreeConstruction import DistanceCalculator, DistanceTreeConstructor
from Bio import Phylo
from Bio import AlignIO
import matplotlib.pyplot as plt


def build_phylogenetic_tree(file_path, method):
    # Step 1: Load sequences
    alignment = AlignIO.read(file_path, "fasta")

    # Step 2: Calculate distance matrix
    calculator = DistanceCalculator('identity')
    distance_matrix = calculator.get_distance(alignment)

    print("\n=== Distance Matrix ===\n")
    print("\nFormatted Distance Matrix:\n")
    for row in str(distance_matrix).split("\n"):
        print("   ", row)

    # Step 3: Build tree
    constructor = DistanceTreeConstructor()

    if method == "upgma":
        tree = constructor.upgma(distance_matrix)
    else:
        tree = constructor.nj(distance_matrix)

    # Root the tree
    tree.rooted = True

    # Step 4: ASCII Tree
    print("\n=== Phylogenetic Tree (ASCII) ===\n")
    Phylo.draw_ascii(tree)

    # Step 5: Save tree image
    print("\nSaving tree as phylogenetic_tree.png ...")
    Phylo.draw(tree, do_show=False)
    plt.savefig("phylogenetic_tree.png", dpi=300, bbox_inches='tight')
    plt.close()

    print("✅ Tree saved successfully!\n")


# -------- RUN PROGRAM --------
if __name__ == "__main__":
    print("\n🌳 Phylogenetic Tree Builder\n")

    file_name = input("Enter FASTA file name (example: sequences.fasta): ")

    print("\nChoose method:")
    print("1. UPGMA")
    print("2. Neighbor Joining")

    choice = input("Enter choice (1/2): ")

    if choice == "1":
        method = "upgma"
    else:
        method = "nj"

    build_phylogenetic_tree(file_name, method)