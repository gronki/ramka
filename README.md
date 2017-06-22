# ramka

Generates nice framed comments to paste into your code.

## Installation

```sh
python setup.py install --user
```

## Usage

```sh
cat - | ramka <<EOF
-- FRAME
this is a frame test!
--
EOF
```

Result:

```fortran
!----------------------------------- FRAME ------------------------------------!
!                            this is a frame test!                             !
!------------------------------------------------------------------------------!
```

To comment fortran code:

```
[user@host ~]$ ramka-fort
Procedure name: calcmx
Description: Calculates matrix coefficients
Inputs (separated by ';') a: input vector; n: vector size
Outputs (separated by ';') M: output matrix (nxn); errno: error code
Return value:
Copyright holder: Jan Nowak
```

Result:

```fortran
!----------------------------------- CALCMX -----------------------------------!
!                        Calculates matrix coefficients                        !
!----------------------------------- INPUTS -----------------------------------!
!                               a: input vector                                !
!                               n: vector size                                 !
!---------------------------------- OUTPUTS -----------------------------------!
!                              M: output matrix (nxn)                          !
!                          errno: error code                                   !
!----------------------------- (c) 2017 Jan Nowak -----------------------------!
```
