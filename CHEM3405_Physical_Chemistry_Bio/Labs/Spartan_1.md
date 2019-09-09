**Computer lab – Spartan 1 \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_**

**Goal**: The goal of this exercise is to familiarize yourself with Spartan, and the kind of information you can get using it.

**Introduction**

In class, we have been discussing wavefunction solutions ψ(*x*) to Schrödinger’s Equation, *H*ψ = Eψ, for an electron as a function of its position *x*. Computational chemistry programs approximate solutions to Schrödinger Equation, but for multi-electron systems—atoms and molecules:

$\\hat{H}$ψ(*x*<sub>1</sub>, *x*<sub>2</sub>,…*x<sub>n</sub>*) = *E*ψ(*x*<sub>1</sub>, *x*<sub>2</sub>,…*x<sub>n</sub>*).

It turns out that if you assume the electrons do not interact (i.e. do not feel each others’ repulsion), then the wave function is *separable*, i.e. solutions are products of one-electron wavefunctions ψ(*x*<sub>1</sub>, *x*<sub>2</sub>,…*x<sub>n</sub>*) = ψ<sub>1</sub>(*x*<sub>1</sub>) ψ<sub>2</sub>(*x*<sub>2</sub>)… ψ*<sub>n</sub>*(*x<sub>n</sub>*). The ψ*<sub>i</sub>* are called *orbitals. *

Quantum chemistry methods try to solve for ψ as a product of orbitals, with different ways of approximating the effects of electron interaction. The computed solution is a set of *molecular orbitals* (MOs), each a one-electron wavefunction that can be spread out over the entire molecule.

As you might imagine, MOs are complicated entities, but can be represented as a *superposition* (i.e. a sum) of *atomic orbitals* (AOs), i.e. wavefunctions of electrons bound to a specific nucleus. For reasons of computational efficiency, each AO in turn is (usually) represented by superposition of simpler functions called *basis functions*. The more basis functions you use, the better the approximation, but at increased computational cost.

In this lab we will explore the effects of using different *basis sets* (i.e. groups of basis functions) for an atomic orbital calculation. We will consider three different basis sets, STO-3G, 3-21G, and 6-31G\* (Figure 1).

**Directions **

1.  Login to your account by using your tuid and password.

2.  Open Spartan by clicking on its icon on the desktop.

3.  File &gt; New Build (or click icon on upper left)

4.  Build an oxygen **atom**:

    1.  Select oxygen from panel and click anywhere in main window.

    2.  Remove bonds by using delete tool (build &gt; delete, or select eraser icon in the panel. You have to click it each time you want to delete an atom)

5.  Setup &gt; Calculations… Parameters:

    1.  **Energy** at **ground** state

    2.  With **Hartree-Fock STO-3G** in **vacuum**, total charge: **neutral, zero unpaired electrons**

    3.  Check box for **orbital and energy**

    4.  Check box for **charges and bond orders**

    5.  Submit (it will ask you where to save the data, it is good to give them proper names and save them on Desktop).

    6.  Wait until calculation is done (a few seconds).

6.  Display &gt; orbital energies

    1.  Record approximate HOMO and LUMO energies (click on spectrum to get values)

7.  Display &gt; Surfaces:

    1.  Add HOMO, LUMO and Electrostatic potential map

    2.  Look at different shape of HOMO, LUMO and electrostatic potential map by clicking on boxes next to them (Do this one by one).

    3.  Close this window.

8.  Display &gt; output:

    1.  Record values for Basis set, HOMO, LUMO, and total energy in **Results** section below

9.  Repeat calculations for these basis sets: STO-3G, 3-21G, 6-31G\* and with these multiplicities: **Singlet** (choose 0 unpaired electrons) and **triplet (**choose 2 unpaired electrons, report “a” and “b” HOMO and LUMOs)

**About energies:** the ground state of H-atom is -13.6 eV = ½ hartree.

1 hartree = 27.2 eV

**Results**

| Basis set | Unpaired electrons | Multiplicity | HOMO energy 
                 
    (eV)         | LUMO energy 
                  
     (eV)         | Total Energy (eV) |
|-----------|--------------------|--------------|-------------|-------------|-------------------|
| STO-3G    | 0                  | singlet      |             |             |                   |
| 3-21G     | 0                  | singlet      |             |             |                   |
| 6-31G\*   | 0                  | singlet      |             |             |                   |
| STO-3G    | 2                  | triplet      |             |             |                   |
| 3-21G     | 2                  | triplet      |             |             |                   |
| 6-31G\*   | 2                  | triplet      |             |             |                   |

**
**

**Figure 1.** Radial functions in basis sets STO-3G, 3-21G, and 6-31G\* for (a) hydrogen and (b) carbon. Plots taken from http://www.chemgapedia.de

|     |                                                         |     |                                                         |
|-----|---------------------------------------------------------|-----|---------------------------------------------------------|
| (a) | <img src="media/image1.gif" width="231" height="372" /> | (b) | <img src="media/image2.gif" width="192" height="346" /> |

Checklist:

1.  Effect of basis set on calculations.

2.  Effect of multiplicity on calculations.

3.  Relative energies of HUMO and LUMO.

4.  Electron Density (from electrostatic potential map)
