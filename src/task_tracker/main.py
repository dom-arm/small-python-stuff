from database import get_collection
from bson import ObjectId


def add_task():
    title = input("Title: ")
    description = input("Description: ")

    add_to_collection(title, description)


def add_to_collection(title, description, status="To Do"):
    collection_name = get_collection()

    collection_name.insert_one(
        {"title": title, "description": description, "status": status}
    )


def list_tasks():
    collection_name = get_collection()
    item_details = collection_name.find()
    print(item_details)

    for item in item_details:
        print(f"🔷\tID: {item['_id']}")
        print(f"\tTitle: {item['title']}")
        print(f"\tDescription: {item['description']}")
        print(f"\tStatus: {item['status']}")


def update_task_status():
    list_tasks()

    task_id = input("Which task status to update? >>> ")
    new_status = (
        "Done"
        if input('Update to "Done" [d] or to "To Do" [t] >>> ') == "d"
        else "To Do"
    )

    update_document(task_id, new_status)


def update_document(task_id, new_status):
    collection_name = get_collection()

    collection_name.update_one(
        {"_id": ObjectId(task_id)}, {"$set": {"status": new_status}}
    )


def delete_task():
    list_tasks()

    task_id = input("Which task to remove? >>> ")
    confirm = input(f"Are you sure you want to remove task {task_id}? [y/n]\n")
    if confirm != "n":
        delete_document(task_id)


def delete_document(task_id):
    collection_name = get_collection()
    collection_name.delete_one({"_id": ObjectId(task_id)})


def prompt():
    print("---------------------")
    option = input(
        "Choose an option:\nAdd a task [1]\nList tasks [2]\nUpdate task status [3]\nRemove a task [4]\n--> Or do you want to exit the task manager? [x]\nOption >>> "
    )
    print("---------------------")
    return option.lower()


def main():
    while True:
        option = prompt()

        if option == "1":
            add_task()
        elif option == "2":
            list_tasks()
        elif option == "3":
            update_task_status()
        elif option == "4":
            delete_task()
        else:
            confirm = input("Are you sure you want to exit? [y/n]\n")
            if confirm != "n":
                print("The task manager is signing out. Thank you for this time! Bye.")
                break


main()
