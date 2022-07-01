#!/bin/sh
wget "https://github.com/runelite/launcher/releases/download/2.4.2/RuneLite.jar"
touch run-runelite.sh && echo "#!/bin/sh" >> run-runelite.sh && echo -ne "java -jar " >> run-runelite.sh && echo -ne "Runelite.jar" >> run-runelite.sh && echo -ne "RuneLite.jar" >> run-runelite.sh && printf "File output--\n" && printf "\n" && cat run-runelite.sh && printf "\n" && printf "\n" && echo "Look good?"

PS3='Pick a Number: '
choices=("Yes" "No/Remove" "Quit")
select choice in "${choices[@]}"; do
    case $choice in
        "Yes")
            chmod +x run-runelite.sh && echo "To launch type ./run-runelite.sh"
            break
	    # optionally call a function or run some code here
            ;;
        "No/Remove")
            echo "Deleting.." && rm run-runelite.sh && echo "Done.. Restart me"
	    # optionally call a function or run some code here
	    break
            ;;
	"Quit")
	    echo "User requested exit"
	    exit
	    ;;
        *) echo "invalid option $REPLY";;
    esac
done

