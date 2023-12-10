#!/bin/sh


#=================================================================
cd AC/
echo "Verifying AC..."

python3 Verify-AC-sex.py
python3 Verify-AC-race.py
python3 Verify-AC-marital.py

echo "AC Done!"
cd ..
#=================================================================
cd BD/
echo "Verifying BD..."

python3 Verify-BD-age.py
python3 Verify-BD-edu.py
python3 Verify-BD-housing.py
python3 Verify-BD-marital.py

echo "BD Done!"
cd ..
#=================================================================
cd BM/
echo "Verifying BM..."

python3 Verify-BM-age.py
python3 Verify-BM-loan.py

echo "BM Done!"
cd ..
#=================================================================
cd CF/
python3 Verify-CF-v24.py

echo "CF Done!"
cd ..
#=================================================================
echo "All Done!"
